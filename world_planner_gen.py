#!/usr/bin/python
"""
@cernodile/py-deltaparser

A Python script to convert Growtopia's items.dat to human-readable indexable format.
File: world_planner_gen.py
Purpose: To generate world data file for Cernodile's World Planner (updated by healLV)
License: See LICENSE.txt in project root directory.
"""
import json
import item_parser
from datatables import PlannerTypes

def filter_web_planner(item):
	"""Filters out items that you should not be able to use in a world planner - be it broken items or illegals."""
	if item.ID % 2 == 1:
		return False
	if item.Type == 0 or item.Type == 1 or item.Type == 4 or item.Type == 8 or item.Type == 19 \
		or item.Type == 20 or item.Type == 37 or item.Type == 44 or item.Type == 64 or item.Type == 107 \
		or item.Type == 112 or item.Type == 114 or item.Type == 129:
		return False

	if "null_item" in item.Name:
		return False

	if (item.ID >= 5822 and item.ID <= 5828) or  (item.ID >= 5834 and item.ID <= 5932) or \
	(item.ID >= 8624 and item.ID <= 8626) or (item.ID >= 8630 and item.ID <= 8632) or \
	(item.ID >= 8642 and item.ID <= 8644) or (item.ID >= 8648 and item.ID <= 8650) or \
	(item.ID >= 8654 and item.ID <= 8656) or (item.ID >= 8660 and item.ID <= 8662) or \
	(item.ID >= 8666 and item.ID <= 8668) or (item.ID >= 8672 and item.ID <= 8674) or \
	(item.ID >= 8678 and item.ID <= 8680) or (item.ID >= 8684 and item.ID <= 8686) or \
	(item.ID >= 8690 and item.ID <= 8692) or (item.ID >= 8696 and item.ID <= 8698) or \
	(item.ID >= 8702 and item.ID <= 8704) or (item.ID >= 8708 and item.ID <= 8710) or \
	(item.ID >= 8714 and item.ID <= 8716) or (item.ID >= 9674 and item.ID <= 9678) or \
	(item.ID >= 8776 and item.ID <= 8792) or (item.ID >= 8636 and item.ID <= 8638) or \
	item.ID == 9640 or item.ID == 244 or item.ID == 660 or item.ID == 5996 or item.ID == 7194:
		return False

	return True

def write_world_planner_data(items):
	web_planner_data_json = {}
	web_planner_data_json["Block Glue"] = {"spread": 1, "file": "tiles_page3.png", "cat": "Glue", "col": 0, "x": 1, "y": 7, "priority": True}
	web_planner_data_json["Enchanted Spatula"] = {"spread": 2, "file": "tiles_page4.png", "cat": "Flip", "col": 0, "x": 14, "y": 7, "priority": True}
	web_planner_data_json["Water"] = {"spread": 2, "file": "water.png", "cat": "Water", "col": 0, "x": 0, "y": 0, "priority": True}
	web_planner_data_json["Fire"] = {"spread": 2, "file": "fire.png", "cat": "Water", "col": 0, "x": 0, "y": 0, "priority": True}
	web_planner_data_json["Paint Bucket - Red"] = {"spread": 1, "file": "paint.png", "cat": "Paint", "col": 0, "x": 0, "y": 0, "priority": True}
	web_planner_data_json["Paint Bucket - Yellow"] = {"spread": 1, "file": "paint.png", "cat": "Paint", "col": 0, "x": 1, "y": 0, "priority": True}
	web_planner_data_json["Paint Bucket - Green"] = {"spread": 1, "file": "paint.png", "cat": "Paint", "col": 0, "x": 2, "y": 0, "priority": True}
	web_planner_data_json["Paint Bucket - Aqua"] = {"spread": 1, "file": "paint.png", "cat": "Paint", "col": 0, "x": 3, "y": 0, "priority": True}
	web_planner_data_json["Paint Bucket - Blue"] = {"spread": 1, "file": "paint.png", "cat": "Paint", "col": 0, "x": 0, "y": 1, "priority": True}
	web_planner_data_json["Paint Bucket - Purple"] = {"spread": 1, "file": "paint.png", "cat": "Paint", "col": 0, "x": 1, "y": 1, "priority": True}
	web_planner_data_json["Paint Bucket - Charcoal"] = {"spread": 1, "file": "paint.png", "cat": "Paint", "col": 0, "x": 2, "y": 1, "priority": True}
	web_planner_data_json["Paint Bucket - Varnish"] = {"spread": 1, "file": "paint.png", "cat": "Paint", "col": 0, "x": 3, "y": 1, "priority": True}

	for item in items:
		# WEB PLANNER DATA	
		if filter_web_planner(items[item]):
			ID = items[item].ID
			web_planner_data_json[items[item].Name] = {
				"spread": items[item].StorageType,
				"file": items[item].FileName.replace("rttex", "png"),
				"cat": "",
				"col": items[item].CollisionType,
				"flip": 1 if items[item].Properties & 0x01 else 0,
				"x": items[item].TexX,
				"y": items[item].TexY
			}
			obj = web_planner_data_json[items[item].Name]
			if items[item].Type < len(PlannerTypes):
				obj["cat"] = PlannerTypes[items[item].Type]
			else:
				print(f"out of range index for webplanner on item {items[item].Name} (ID:{items[item].ID}): {items[item].Type}")
			# exceptions
			if items[item].Properties & 0x400:
				obj["cat"] = "RESTRICTED"
			if ID == 396 or ID == 1908 or ID == 1910 or ID == 1912 or ID == 6852:
				obj["cat"] = "RESTRICTED"

			if ID >= 2242 and ID <= 2250:
				obj["file"] = "crystals.png"
				obj["y"] = 1 if ID == 2250 else 0
				obj["x"] = (ID - 2242) // 2 if ID != 2250 else 0

			# Should really remap the file to be easily divisible like crystals above.
			if ID >= 4382 and ID <= 4398:
				obj["file"] = "bunting.png"
				obj["x"] = obj["y"] = 0
			if ID == 4384 or ID == 4388 or ID == 4392:
				obj["x"] = 4
			if ID == 4386 or ID == 4388:
				obj["y"] = 1
			if ID == 4390 or ID == 4392 or ID == 4394:
				obj["y"] = 2
			if ID == 4394:
				obj["x"] = 6
			if ID == 4396 or ID == 4398:
				obj["y"] = 3
			if ID == 4398:
				obj["x"] = 2

			if ID == 620 or ID == 3592:
				obj["file"] = "pipes.png"
				obj["x"] = 0
				obj["y"] = 0 if ID == 620 else 2

			if ID == 3558:
				obj["y"] = obj["y"] + 1

			if ID == 5814:
				obj["file"] = "guild_lock.png"
				obj["x"] = obj["y"] = 0
			
	web_planner_data = open("web_planner.json", "w")
	web_planner_data.write(f"data = {json.JSONEncoder(indent=4).encode(web_planner_data_json)}")
	web_planner_data.close()

if __name__ == '__main__':
	items = item_parser.parse("items.dat")
	write_world_planner_data(items)
