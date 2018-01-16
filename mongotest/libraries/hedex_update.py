from libraries.primary_keys import PrimaryKeys
from libraries.dict_funcs import DictFuncs

class HedexUpdate(object):
    
    @classMethod
    def update_array_by_pk(self, the_array, update_dict, primary_keys):
        # Type checks
        if not DictFuncs.is_sequence(theArray):
            raise ValueError("updateArrayByPK requires a list/tuple as the first parameter")
        if not isinstance(update_dict, dict):
            raise ValueError("updateArrayByPK requires a dict as the second parameter")
        # We're going to loop over all the items in theArray
        # We want to keep track of whether an iterm was updated
        wasUpdated = False
        # Start the loop
        for obj in the_array:
            # Another type check
            if not isinstance(obj, dict):
                raise ValueError("updateArrayByPK requires the members of the second parameter to be dicts")
            # Check primary keys
            if self._check_pks(obj, primary_keys):
                # If a primary key on this object matched the update_obj, the update the obj
                self._do_update(obj, update_dict, primary_keys)
            else:
                # If we didn't update an item in the list, add the whole update_dict as a new item
                theArray.append(update_dict)
    
    
    @classMethod
    def _check_pks(self, obj, update_obj, primary_keys):
        # The "_" element of the primary_keys dict is the list of primary keys consisting of tuples
        for p in primary_keys["_"]:
            if self._check_pk(obj, update_obj, tup):
                return True
    
    
    @classMethod
    def _check_pk(self, obj, update_obj, tup):
        # Each primary key is a list of tuples
        for tup in p:
            # The name of the primary key column is the element 0
            p_name = tup[0]
            # The type is element 1
            p_type = tup[1]
            # The optional element 2 is the default value
            # If it is expressly set to None, then a None is an allowed value in a PK
            p_none_ok = False
            try:
                p_default = tup[2]
                if p_default == None:
                    p_none_ok = True
            except:
                if pType == "boolean":
                    p_default = False
                else:
                    p_default = None
            # Get the value
            o_val = obj[p_name] if p_name in obj else p_default
            if o_val == None and not p_none_ok:
                return False
            u_val = update_obj[p_name] if p_name in update_obj else p_default
            if o_val != u_val:
                return False
        return True
    
    
    @classMethod
    def do_update(self, obj, update_dict, primary_keys):
        for key, val in update_dict.items():
            # If the value is a list/tuple
            if DictFuncs.is_sequence(val):
                # We should know about this in the object structure mapping
                if key not in primary_keys:
                    raise ValueError("unexpected key " + key + " found in object nesting")
                if key in obj:
                    # If it's in the object we're updating, we need to recur to update it
                    self.update_array_by_pk(obj[key], val, primary_keys[key])
                else:
                    # If it's not, then we need to add it
                    obj[key] = update_dict[key]
            elif isinstance(val, dict):
                # If it's a dictionary, then we have a one-to-one sub
                # We should know about this in the object structure mapping
                if key not in primary_keys:
                    raise ValueError("unexpected one-to-one key " + key + " found in object nesting")
                if key in obj:
                    # If the key is there, we simply update it - no need to search!
                    self.do_update(obj[key], val, primary_keys[key])
            elif val == None:
                # This means to remove the item from the structure
                obj.pop(key, None)
            else:
                # It's just a normal object, not in object mapping
                obj[key] = update_dict[key]


