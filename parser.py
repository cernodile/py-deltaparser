"""
@cernodile/py-deltaparser

A Python script to convert Growtopia's items.dat to human-readable indexable format.
File: parser.py
Purpose: The actual parser for items.
License: See LICENSE.txt in project root directory.
"""
max_version = 12
class Item:
	def __init__(self):
		self.ID = 0
		self.Properties = 0
		self.Type = 0
		self.Material = 0
		self.Name = ""
		self.FileName = ""
		self.FileHash = -1
		self.VisualType = 0
		self.Unk = 0
		self.TexX = 0
		self.TexY = 0
		self.StorageType = 0
		self.Layer = 0
		self.CollisionType = 0
		self.Hardness = 0
		self.RegenTime = 0
		self.ClothingType = 0
		self.Rarity = 999
		self.MaxHold = 200
		self.AltFilePath = ""
		self.AltFileHash = -1
		self.AnimMS = 0
		self.PetName = ""
		self.PetPrefix =""
		self.PetSuffix = ""
		self.PetAbility = ""
		self.SeedBase = 0
		self.SeedOver = 0
		self.TreeBase = 0
		self.TreeOver = 0
		self.BgCol = 0
		self.FgCol = 0
		self.Unk2 = 0
		self.BloomTime = 31
		self.AnimType = 0
		self.AnimString = ""
		self.AnimTex = ""
		self.AnimString2 = ""
		self.DLayer1 = 0
		self.DLayer2 = 0
		self.Properties2 = 0
		self.TileRange = 0
		self.PileRange = 0
		self.CustomPunch = ""

def decrypt_name(Name, cryptID):
	"""Ported from Proton SDK @ ResourceUtils.cpp."""
	secretCode = "PBG892FXX982ABC*"
	codeLen = len(secretCode)
	cryptID %= codeLen
	new_name = ""
	for letter in Name:
		b = ord(letter) ^ ord(secretCode[cryptID])
		cryptID += 1
		new_name += chr(b)
		if cryptID >= codeLen:
			cryptID = 0
	return new_name

def parse_string(buf):
	len = int.from_bytes(buf.read(2), 'little')
	return buf.read(len).decode("utf-8")

def parse(file_name: str):
	items = {}
	try:
		file = open(file_name, "rb")
		version = int.from_bytes(file.read(2), 'little')
		if version > max_version:
			print(f"WARNING! You are attempting to parse an items.dat with unsupported database version. Latest supported is {max_version} while this file is {version}. This will 99% likely fail.")
		item_count = int.from_bytes(file.read(4), 'little')
		for i in range(0, item_count):
			item = Item()
			item.ID = int.from_bytes(file.read(4), 'little')
			item.Properties = int.from_bytes(file.read(2), 'little')
			item.Type = int.from_bytes(file.read(1), 'little')
			item.Material = int.from_bytes(file.read(1), 'little')
			item.Name = parse_string(file)
			if version >= 3:
				item.Name = decrypt_name(item.Name, item.ID)
			item.FileName = parse_string(file)
			item.FileHash = int.from_bytes(file.read(4), 'little')
			item.VisualType = int.from_bytes(file.read(1), 'little')
			item.Unk = int.from_bytes(file.read(4), 'little')
			item.TexX = int.from_bytes(file.read(1), 'little')
			item.TexY = int.from_bytes(file.read(1), 'little')
			item.StorageType = int.from_bytes(file.read(1), 'little')
			item.Layer = int.from_bytes(file.read(1), 'little')
			item.CollisionType = int.from_bytes(file.read(1), 'little')
			item.Hardness = int.from_bytes(file.read(1), 'little')
			item.RegenTime = int.from_bytes(file.read(4), 'little')
			item.ClothingType = int.from_bytes(file.read(1), 'little')
			item.Rarity = int.from_bytes(file.read(2), 'little')
			item.MaxHold = int.from_bytes(file.read(1), 'little')
			item.AltFilePath = parse_string(file)
			item.AltFileHash = int.from_bytes(file.read(4), 'little')
			item.AnimMS = int.from_bytes(file.read(4), 'little')
			if version >= 4:
				item.PetName = parse_string(file)
				item.PetPrefix = parse_string(file)
				item.PetSuffix = parse_string(file)
				if version >= 5:
					item.PetAbility = parse_string(file)
			item.SeedBase = int.from_bytes(file.read(1), 'little')
			item.SeedOver = int.from_bytes(file.read(1), 'little')
			item.TreeBase = int.from_bytes(file.read(1), 'little')
			item.TreeOver = int.from_bytes(file.read(1), 'little')
			item.BgCol = int.from_bytes(file.read(4), 'little')
			item.FgCol = int.from_bytes(file.read(4), 'little')
			item.Unk2 = int.from_bytes(file.read(4), 'little')
			item.BloomTime = int.from_bytes(file.read(4), 'little')
			if version >= 7:
				item.AnimType = int.from_bytes(file.read(4), 'little')
				item.AnimString = parse_string(file)
			if version >= 8:
				item.AnimTex = parse_string(file)
				item.AnimString2 = parse_string(file)
				item.DLayer1 = int.from_bytes(file.read(4), 'little')
				item.DLayer2 = int.from_bytes(file.read(4), 'little')
			if version >= 9:
				item.Properties2 = int.from_bytes(file.read(4), 'little')
				# clientdata, never really relevant, skip over.
				file.read(4 * 15)
			if version >= 10:
				item.TileRange = int.from_bytes(file.read(4), 'little')
				item.PileRange = int.from_bytes(file.read(4), 'little')
			if version >= 11:
				CustomPunch = parse_string(file)
			if version >= 12:
				# not really useful data, fixed size, can skip.
				file.read(13)
			items[item.ID] = item
		return items
	except FileNotFoundError:
		print("Couldn't find item data file.")
