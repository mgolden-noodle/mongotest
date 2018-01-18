#!/usr/bin/python3

from sys import argv
import logging
import json
from libraries.update_hedex import UpdateHedex
from libraries.primary_keys import PrimaryKeys

pkl_file_path = "data"

if argv.__len__() != 2:
    print("usage: start filename\n")
    exit(1)

file_name = argv[1]
try:
    call = file_name[file_name.index("_"):]
    call = call[1:call.rindex(".")]
except:
    print("file_name must be .../GET_SOME_HEDEX_CALL.json or .../POST_SOME_HEDEX_CALL.json. Was %s" % file_name)
    exit(1)

if call not in PrimaryKeys.primary_keys:
    print("file_name must be .../GET_SOME_HEDEX_CALL.json or .../POST_SOME_HEDEX_CALL.json, where SOME_HEDEX_CALL is one of:")
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
