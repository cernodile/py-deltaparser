#!/usr/bin/python
"""
@cernodile/py-deltaparser

A Python script to convert Growtopia's items.dat to human-readable indexable format.
File: item_json_generator.py
Purpose: To generate data file for general viewing.
License: See LICENSE.txt in project root directory.
"""
import json
import item_parser

def write_json_data_file(items):
	obj = {}
	for item in items:
		item = items[item]
		if item.ID % 2 == 1:
			obj[item.ID - 1]["growtime"] = item.BloomTime 
			obj[item.ID - 1]["bgColor"] = item.BgCol
			obj[item.ID - 1]["fgColor"] = item.FgCol
			continue
		obj[item.ID] = {
			"name": item.Name,
			"type": item.Type,
			"properties": item.Properties,
			"properties2": item.Properties2,
			"material": item.Material, # sound/etc for it
			"file": item.FileName,
			"fileX": item.TexX,
			"fileY": item.TexY,
			"spread": item.StorageType,
			"visual": item.VisualType,
			"hardness": item.Hardness,
			"collision": item.CollisionType,
			"rarity": item.Rarity,
			"regentime": item.RegenTime
		}
		if item.AltFilePath != "":
			obj[item.ID]["extraString"] = item.AltFilePath
		if item.Type == 20:
			obj[item.ID]["clothingType"] = item.ClothingType
		if item.MaxHold != 200:
			obj[item.ID]["maxHold"] = item.MaxHold

	item_file = open("items.json", "w")
	item_file.write(json.JSONEncoder(indent=4).encode(obj))
	item_file.close()

if __name__ == '__main__':
	items = item_parser.parse("items.dat")
	write_json_data_file(items)
