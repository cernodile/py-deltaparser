#!/usr/bin/python
"""
@cernodile/py-deltaparser

A Python script to convert Growtopia's items.dat to human-readable indexable format.
File: main.py
Purpose: This file is the typical "create it all" file.
License: See LICENSE.txt in project root directory.
"""
import json
import parser
from world_planner_gen import write_world_planner_data
from iamim_gt_planner import write_iamim_gt_planner

items = parser.parse("items.dat")
name_file_json = {}
for item in items:
	name_file_json[item] = items[item].Name

name_file = open("names.json", "w")
name_file.write(json.JSONEncoder(indent=4).encode(name_file_json))
name_file.close()

write_world_planner_data(items)
write_iamim_gt_planner
