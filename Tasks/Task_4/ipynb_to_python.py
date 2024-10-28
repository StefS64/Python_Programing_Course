import json
import random 


# Initialized keys and data specifikation.
keys = ["Model", "Output value", "Time of computation"]
bounds = [['A','C'], [0, 1000], [0, 1000]]


# Function returns computation time in case of error returns -1.
def read_json_file(json_file):
	# Quick validation of JSON file structure.
	with open(json_file, "r") as read_file:
		data = json.load(read_file)
		print(data)	

file = input()
print(read_json_file(file))

