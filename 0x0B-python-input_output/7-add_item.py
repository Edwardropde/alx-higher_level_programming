#!/usr/bin/python3
"""Script to add arguments to a Python list and save them to a JSON file."""
import sys
import os.path

# Importing the save_to_json_file and load_from_json_file functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Check if the JSON file exists, if not, create an empty list
filename = "add_item.json"
my_list = []

if os.path.isfile(filename):
    my_list = load_from_json_file(filename)

# Append command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(my_list, filename)
