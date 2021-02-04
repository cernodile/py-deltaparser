#!/usr/bin/python
"""
@cernodile/py-deltaparser

A Python script to convert Growtopia's items.dat to human-readable indexable format.
File: iamim_gt_planner.py
Purpose: To generate data file for Iamim's GT Planner
License: See LICENSE.txt in project root directory.
"""
import csv
import parser
def filter(item):
	"""Filters out items that you should not be able to use in a world planner."""
	if item.ID % 2 == 1:
		return False
	if item.Type == 0 or item.Type == 1 or item.Type == 4 or item.Type == 8 or item.Type == 19 \
		or item.Type == 20 or item.Type == 37 or item.Type == 44 or item.Type == 57 or item.Type == 64 or item.Type == 107 \
		or item.Type == 112 or item.Type == 120 or item.Type == 129:
		return False

	# Any bedrock-type that is within startopia
	if item.Type == 15 and item.ID > 6000 and item.ID <= 6742:
		return False

	if "null_item" in item.Name:
		return False

	if "Guild Flag" in item.Name:
		return False

	# Blank, UPDATE_STORE, Valhowla Treasure
	if item.ID == 0 or item.ID == 244 or item.ID == 4368:
		return False
	return True

def get_item_type(Type):
	if Type == 18 or Type == 22 or Type == 23 or Type == 28:
		return "Background"
	return "Foreground"

def get_informational_type(item):
	if item.Type == 7:
		return "Bouncy"
	elif item.Type == 2 or item.Type == 13 or item.Type == 26:
		return "Door"
	elif item.Type == 3:
		return "Lock"
	elif item.Type == 6 or item.Type == 45 or item.Type == 93:
		return "Death"
	elif item.Type == 9:
		return "Entrance"
	elif item.Type == 10:
		return "Sign"
	elif item.Type == 12 or item.Type == 31 or item.Type == 32 or item.Type == 122:
		return "Togglable Block"
	elif item.Type == 14 or item.CollisionType == 2:
		return "Platform"
	elif item.Type == 16 or item.Type == 25 or item.Type == 126 or item.Type == 136 or item.ID == 5238:
		return "Pain"
	elif item.Type == 27:
		return "Checkpoint"
	elif item.Type == 28:
		return "Music Note"
	elif item.Type == 41 or item.Type == 81 or item.Type == 89 or item.Type == 134:
		return "Weather Machine"
	elif item.Type == 60:
		return "Wind"
	elif item.Type == 69 or item.Type == 70 or item.Type == 71 or item.Type == 79:
		return "Steam"
	elif item.Type == 113:
		return "Bots"
	else:
		return get_item_type(item.Type)

def get_special_data(item):
	name = item.FileName.replace(".rttex", "")
	x = item.TexX
	y = item.TexY
	if (item.ID >= 3258 and item.ID <= 3268) or item.ID == 3280 or item.ID == 3282 or item.ID == 3412 or item.ID == 3414 \
		or (item.ID >= 3752 and item.ID <= 3756) or item.ID == 3766 or item.ID == 3768:
		name = "Steam_items"
		x = 0
		y = 0
		if item.ID == 3258 or item.ID == 3268 or item.ID == 3412 or item.ID == 3756:
			x = 8
		if item.ID == 3262 or item.ID == 3280 or item.ID == 3766 or item.ID == 3768:
			x = 16
		if item.ID == 3264 or item.ID == 3282 or item.ID == 3752:
			x = 24
		if item.ID >= 3268 and item.ID <= 3282:
			y = 6
		if item.ID == 3412 or item.ID == 3414 or item.ID == 3752 or item.ID == 3766:
			y = 12
		if item.ID == 3754 or item.ID == 3756 or item.ID == 3768:
			y = 18
	if item.ID == 620 or item.ID == 3592:
		name = "pipes"
		x = 0
		y = 0 if item.ID == 620 else 2
	if item.ID >= 2242 and item.ID <= 2250:
		name = "crystals"
		y = 1 if item.ID == 2250 else 0
		x = (item.ID - 2242) // 2 if item.ID != 2250 else 0
	if item.ID >= 4382 and item.ID <= 4398:
		name = "bunting"
		x = y = 0
		if item.ID == 4384:
			x = 4
		elif item.ID == 4386:
			y = 1
		elif item.ID == 4388:
			x = 4
			y = 1
		elif item.ID == 4390:
			y = 2
		elif item.ID == 4392:
			x = 4
			y = 2
		elif item.ID == 4394:
			x = 6
			y = 2
		elif item.ID == 4396:
			y = 3
		elif item.ID == 4398:
			x = 2
			y = 3
	if item.ID == 9516:
		name = "Dining"
	return (name, x, y)


def write_iamim_gt_planner(items):
	with open("iamim_gt_planner.csv", "w") as csvfile:
		writer = csv.writer(csvfile, delimiter="|")
		writer.writerow([1, "Water", "Water", 2, "Water", "Water", 0, 0, 0])
		for item in items:
			item = items[item]
			if filter(item):
				data = get_special_data(item)
				writer.writerow([item.ID, item.Name, get_item_type(item.Type), item.StorageType, get_informational_type(item), data[0], data[1], data[2], 1 if item.Properties & 0x01 else 0])
				# actual 4660 is a confetti cannon, 5604 a goldfish bowler hat.
				if item.ID == 4658:
					writer.writerow([4660, "Detonated Uranium Block", "Foreground", 1, "Foreground", "tiles_page10", 3, 1, 0])
				elif item.ID == 5602:
					writer.writerow([5604, "Drilled Ice Crust Block", "Foreground", 1, "Foreground", "tiles_page9", 7, 0, 0])
				elif item.ID == 7866:
					writer.writerow([7865, "Topiary Hedge (Swirly)", "Foreground", 1, "Foreground", "tiles_page13", 28, 11, 1])
					writer.writerow([7866, "Topiary Hedge (Bird)", "Foreground", 1, "Foreground", "tiles_page13", 26, 11, 1])
					writer.writerow([7867, "Topiary Hedge (Circle)", "Foreground", 1, "Foreground", "tiles_page13", 27, 11, 1])
				elif item.ID == 9030:
					writer.writerow([9032, "Spooky Bunting (pumpkin)", "Foreground", 1, "Foreground", "tiles_page14", 18, 10, 1])
					writer.writerow([9034, "Spooky Bunting (ghost)", "Foreground", 1, "Foreground", "tiles_page14", 19, 10, 1])
					writer.writerow([9036, "Spooky Bunting (bats)", "Foreground", 1, "Foreground", "tiles_page14", 21, 10, 1])
				elif item.ID == 9198:
					writer.writerow([9199, "Ice Sculptures (Flower)", "Foreground", 1, "Foreground", "tiles_page14", 9, 12, 0])
				elif item.ID == 9200:
					writer.writerow([9201, "Ice Sculptures (Teddy Bear)", "Foreground", 1, "Foreground", "tiles_page14", 10, 12, 0])
				elif item.ID == 9202:
					writer.writerow([9203, "Ice Sculptures (Star)", "Foreground", 1, "Foreground", "tiles_page14", 11, 12, 0])

if __name__ == "__main__":
	items = parser.parse("items.dat")
	write_iamim_gt_planner(items)
