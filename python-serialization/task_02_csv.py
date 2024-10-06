#!/usr/bin/python3
"""
Converting CSV Data to JSON Format
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts CSV data to JSON and writes it to 'data.json'."""
    try:
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)

        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
