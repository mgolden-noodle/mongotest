import logging
import sys
from pymongo import MongoClient, ASCENDING

from libraries.primary_keys import PrimaryKeys

class CreateHedexIndexes(object):

    log_level = logging.DEBUG
    # log_level = logging.ERROR

    debug_log = None
    db = None


    @classmethod
    def my_setup(self):
        format = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s'
        logging.basicConfig(filename=("create_hedex_indexes.log"),format=format, datefmt="%Y-%m-%d %H:%M:%S")
        debug_log = logging.getLogger("create_hedex_indexes")
        debug_log.setLevel(self.log_level)
    
    
    @classmethod
    def init(self):
        client = MongoClient('mongodb://localhost:27017/')  
        self.db = client.hedexdb
        self.my_setup()
        self.debug_log = logging.getLogger("create_hedex_indexes")
    
    
    @classmethod
    def create_hedex_indexes(self):
        if not self.debug_log:
            self.init()
        self.debug_log.debug("Hello %s!", "hi!")
        primary_keys = PrimaryKeys.primary_keys
        for call, val in primary_keys.items():
            name = list(val.keys())[0]
            self.debug_log.debug("call is %s", (call,))
            pks = val[name]["_"]
            indexes = []
            for pk in pks:
                index = []
                for col in pk:
                    index.append((col[0], ASCENDING))
                index_name = name+"_main_index"
                self.debug_log.debug("call is db[%s].create_index(%s,)", name, index)
                self.db[name].create_index(index)
