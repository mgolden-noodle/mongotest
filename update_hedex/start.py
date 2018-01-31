#!/usr/bin/python3

from sys import argv
import logging
import json
import re
import traceback
from libraries.update_hedex import UpdateHedex
from libraries.primary_keys import PrimaryKeys

log_level = logging.DEBUG
# log_level = logging.ERROR


global debug_log
def show_message(message):
    debug_log.error(message)
    print(message)


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
    print(list(PrimaryKeys.primary_keys.keys()))
    print("was %s"%file_name)
    exit(1)

try:
    f = open(file_name, "r")
except:
    print("Can't open %s" % file_name)
    exit(1)

format = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s'
logging.basicConfig(filename=("update_hedex.log"),format=format, datefmt="%Y-%m-%d %H:%M:%S")
debug_log = logging.getLogger("update_hedex")
debug_log.setLevel(log_level)

show_message("file_name is %s, call is %s"%(file_name, call))

json_payload = json.load(f)
f.close()

try:
    UpdateHedex.init()
    UpdateHedex.handle_payload(call, json_payload)
except Exception as ex:
    show_message("Error processing %s" % file_name)
    show_message(''.join(traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__)))
