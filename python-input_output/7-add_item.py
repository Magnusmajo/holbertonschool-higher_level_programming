#!/usr/bin/python3
"""
Load, add, save
"""
import json
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    if os.path.exists('add_item.json'):
        with open('add_item.json', 'r') as f:
            add_arg = json.load(f)
    else:
        add_arg = []
except json.JSONDecodeError as e:
    sys.exit(1)

for i in arg:
    if i not in add_arg:
        add_arg.append(i)

try:
    with open('add_item.json', 'w') as f:
        json.dump(add_arg, f)
except Exception as e:
    sys.exit(1)
