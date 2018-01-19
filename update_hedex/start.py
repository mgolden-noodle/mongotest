#!/usr/bin/python3

from sys import argv
import logging
import json
from libraries.update_hedex import UpdateHedex
from libraries.primary_keys import PrimaryKeys
import re

pkl_file_path = "data"

if argv.__len__() != 2:
    print("usage: start filename")
    exit(1)

file_name = argv[1]
rx1 = re.compile('^(.*/|)(GET_|POST_|)')
rx2 = re.compile('[0-9_]*\.json$')
call = rx1.sub("", file_name)
call = rx2.sub("", call)

if call not in PrimaryKeys.primary_keys:
    print("file_name must be .../SOME_HEDEX_CALL.json. GET_ or POST_ is optional, as is a timestamp. SOME_HEDEX_CALL is one of:")
    print(list(primary_keys.keys()))
    exit(1)

try:
    f = open(file_name, "r")
except:
    print("Can't open %s" % file_name)
    exit(1)

logging.basicConfig(filename=("update_hedex.log"))
debug_log = logging.getLogger("update_hedex")
debug_log.setLevel(logging.DEBUG);

debug_log.debug("call is %s", call)

json_payload = json.load(f)
f.close()

UpdateHedex.handle_payload(call, json_payload, pkl_file_path)
