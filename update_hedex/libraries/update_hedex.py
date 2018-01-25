import logging
from pymongo import MongoClient  

from libraries.primary_keys import PrimaryKeys
from libraries.persist import Persist

class UpdateHedex(object):

    debug_log = None
    client = None
    db = None

    def init():
        client = MongoClient('mongodb://localhost:27017/')  
        db = client.hedexdb

    @classmethod
    def handle_payload(self, call, json_payload, pkl_file_path):
        if not self.debug_log:
            self.debug_log = logging.getLogger("update_hedex")

        # Load the whole json structure for the .pkl file
        self.debug_log.debug("Loading from .pkl file")
        the_array = Persist.load_obj(call, pkl_file_path)
        if not the_array:
            self.debug_log.debug("Nothing loaded from .pkl file")

        # Examine the header. Doesn't do anything for now except call update_hedex
        seq_key = None
        for k, v in json_payload.items():
            self.debug_log.debug("examining key %s" % k)
            if self.is_sequence(v):
                self.debug_log.debug("found a sequence on key %s" % k)
                if seq_key:
                    error = "found two keys in json_payload '%s' and '%s'" % (seq_key, k)
                    self.debug_log.debug(error)
                    raise ValueError(error)
                seq_key = k

        if not seq_key:
            error = "found no keys in json_payload"
            self.debug_log.debug(error)
            raise ValueError(error)

        # iterate over the dictionaires in the value
        to_append = []
        for update_obj in json_payload[seq_key]:
            self._update_mongo_by_pk(update_obj, call, to_append, PrimaryKeys.primary_keys[call][seq_key])
        db.[call].update_many(to_append, ordered=False)

        self.debug_log.debug("saving to .pkl file")
        Persist.save_obj(the_array, call, pkl_file_path)


    @classmethod
    # is this item iterable (but not a string or dict)
    def is_sequence(self, arg):
        return (not hasattr(arg, "strip") and
                not isinstance(arg, dict) and
                (hasattr(arg, "__getitem__") or hasattr(arg, "__iter__")))
    
    
    @classmethod
    def _unpack_tup(self, tup):
        # The name of the primary key column is the element 0
        p_name = tup[0]
        # The optional type is element 1
        l = tup.__len__()
        p_type = tup[1] if l > 1 else "string"
        # The optional element 2 is the default value
        # If it is expressly set to None, then a None is an allowed value in a PK
        p_none_ok = False
        if l > 2:
            p_default = tup[2]
            if p_default == None:
                p_none_ok = True
        else:
            if p_type == "boolean":
                p_default = False
            else:
                p_default = None
        return (p_name, p_type, p_default, p_none_ok)

    
    @classmethod
    def _update_mongo_by_pk(self, update_obj, call, to_append, primary_keys):
        # Type checks
        if not isinstance(update_obj, dict):
            raise ValueError("_update_array_by_pk requires a dict as the first parameter, was %s" % update_obj)
        rows = self._query_pks(update_obj, call, primary_keys)
        if rows:
            # If a primary key on this object matched the update_obj, then update the obj
            self.debug_log.debug("PK matched")
            if rows.__len__() > 1:
                self.debug_log.warn("Warning: %d rows found, should have been 1", rows.__len__())
            row = rows[0]
            self._do_update(row, update_obj, primary_keys)
            db[call].replace_one({"_id": row["_id"]}, row)
        else:
            to_append.append(update_obj)
        

    @classmethod
    def _query_pks(self, update_obj, call, primary_keys):
        # The "_" element of the primary_keys dict is the list of primary keys consisting of tuples
        # Don't check for the existence of this, it has already been checked before invocation
        for pk in primary_keys["_"]:
            x = self._query_pk(obj, update_obj, pk)
            if(x):
                return x
        return []
    

    @classmethod
    def _query_pk(self, update_obj, call, pk):
        # self.debug_log.debug("_query_pk(..., %s)" % p)
        # Each primary key is a list of tuples
        terms = {}
        for tup in pk:
            p_name, p_type, p_default, p_none_ok = self._unpack_tup(tup)
            # Get the value
            u_val = update_obj[p_name] if p_name in update_obj else p_default
            # self.debug_log.debug("name is %s o_val is %s" % (p_name, o_val))
            if u_val == None:
                # If null is not allowed as a PK value, and the object we're looking for has a null
                # in this PK, then it cannot match a row
                if not p_none_ok:
                    # self.debug_log.debug("_query_pk() returns []")
                    return []
                # Note that null is only allowed as a PK value if it's the default.
                # Therefore, if we're searching for a null, a non-existant key will also match.
                terms[p_name] = None
            else if u_val == p_default:
                # The value is the default value, but not null.  Nonexistence will match
                terms["$or"] = [{p_name: u_val}, {p_name: {"$exists": False}}]
            else:
                # The value is not the default value, so only the correct value matches.
                terms[p_name] = u_val
        db
        # self.debug_log.debug("_query_pk() returns True")
        return True
    
    
    @classmethod
    def _update_array_by_pk(self, the_array, update_obj, to_append, primary_keys):
        self.debug_log.debug("_update_array_by_pk(...)")
        # Type checks
        if not self.is_sequence(the_array):
            raise ValueError("_update_array_by_pk requires a list/tuple as the first parameter")
        if not isinstance(update_obj, dict):
            raise ValueError("_update_array_by_pk requires a dict as the second parameter, was %s" % update_obj)
        # We're going to loop over all the items in theArray
        i = 0
        was_updated = False
        for obj in the_array:
            self.debug_log.debug("Examining item %d"%i)
            # Another type check
            if not isinstance(obj, dict):
                raise ValueError("update_array_by_pk requires the members of the second parameter to be dicts; item %d wasn't"%i)
            # Check primary keys
            if self._check_pks(obj, update_obj, primary_keys):
                # If a primary key on this object matched the update_obj, then update the obj
                self.debug_log.debug("PK matched for item %d"%i)
                self._do_update(obj, update_obj, primary_keys)
                was_updated = True
                i += 1  # if we think that there could be two items with the same PK, remove this
                break   # and this
            i += 1
        self.debug_log.debug("Total of %d records processed"%i)
        if not was_updated:
            # If we didn't update an item in the list, add the whole update_obj as a new item
            self.debug_log.debug("PK not matched anywhere, appending")
            to_append.append(update_obj)
    
    
    @classmethod
    def _check_pks(self, obj, update_obj, primary_keys):
        # The "_" element of the primary_keys dict is the list of primary keys consisting of tuples
        # Don't check for the existence of this, it has already been checked before invocation
        for p in primary_keys["_"]:
            if self._check_pk(obj, update_obj, pk):
                return True
        return False
    
    
    @classmethod
    def _check_pk(self, obj, update_obj, pk):
        # self.debug_log.debug("_check_pk(..., %s)" % p)
        # Each primary key is a list of tuples
        for tup in pk:
            p_name, p_type, p_default, p_none_ok = self._unpack_tup(tup)
            # Get the value
            o_val = obj[p_name] if p_name in obj else p_default
            # self.debug_log.debug("name is %s o_val is %s" % (p_name, o_val))
            if o_val == None and not p_none_ok:
                # self.debug_log.debug("_check_pk() returns False")
                return False
            u_val = update_obj[p_name] if p_name in update_obj else p_default
            if o_val != u_val:
                # self.debug_log.debug("_check_pk() returns False")
                return False
        # self.debug_log.debug("_check_pk() returns True")
        return True
    
    
    @classmethod
    def _do_update(self, obj, update_obj, primary_keys):
        self.debug_log.debug("_do_update(...)")
        for key, val in update_obj.items():
            # If the value is a list/tuple
            if self.is_sequence(val):
                # We should know about this in the object structure mapping
                if key not in primary_keys:
                    raise ValueError("unknown child key '" + key + "' found")
                pk_key = primary_keys[key]
                if "_" not in pk_key:
                    raise ValueError("on key '" + key + "' an array was found where a one-to-one child was expected")
                if key in obj:
                    # If this key is in the object we're updating, we need to recur to update it
                    the_sub_array = obj[key]
                    self.debug_log.debug("key is %s", key)
                    to_append = []
                    for sub_val in val:
                        self._update_array_by_pk(the_sub_array, sub_val, to_append, pk_key)
                    the_sub_array += to_append
                else:
                    # If it's not, then we need to add it
                    obj[key] = update_obj[key]
            elif isinstance(val, dict):
                # If it's a dictionary, then we have a one-to-one child
                # We should know about this in the object structure mapping
                if key not in primary_keys:
                    raise ValueError("unexpected one-to-one child on key '" + key + "' found")
                pk_key = primary_keys[key]
                # An "_" element means that this was supposed to be an array
                if "_" in pk_key:
                    raise ValueError("on key '" + key + "' an one-to-one child was found where and array was expected")
                if key in obj:
                    self.debug_log.debug("key is %s", key)
                    # If the key is there, we simply update it - it has no primary key to search for!
                    self._do_update(obj[key], val, pk_key)
            elif val == None:
                # This means to remove the item from the structure
                obj.pop(key, None)
            else:
                # It's just a normal object, not in object mapping
                obj[key] = update_obj[key]
