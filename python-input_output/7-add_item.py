#!/usr/bin/python3
"""
Load, add, save
."""
import sys

from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

try:
    arg = load_from_json_file("add_item.json")
except FileNotFoundError:
    arg = []
    arg.extend(sys.argv[1:])
    save_to_json_file(arg, "add_item.json")
