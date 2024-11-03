import json
import random 

# Program writes specified input into JSON files.
# Program returns Time of computation of a JSON file of proper format.
# In case of error returns -1.

# Initialized keys and data specification.
keys = ["Model", "Output value", "Time of computation"]
bounds = [['A','C'], [0, 1000], [0, 1000]]
is_time = [False, False, True]

# Function checks if variable check is of right type and in the proper bound,
# time type is checked separately.
def within_bounds(check, lower_bound, upper_bound, is_time):
	if is_time == True:
		if not isinstance(check, str) or not check.endswith("s"):
			return "Data type isn't of time type."
		check = int(check[:-1])
	if type(check) != type(lower_bound):
		return "Data type value corresponding to key doesn't match."
	if lower_bound <= check <= upper_bound:
		return "OK"
	else: 
		return "Value corresponding to key is out of bounds."

def error(error_message):
	print("INVALID JSON STRUCTURE!!\n", error_message)
	return -1

def write_json_file(json_file):
    data = {
       	keys[0] : random.choice([chr(i) for i in range(ord(bounds[0][0]), ord(bounds[0][1]) + 1)]),
		keys[1] : random.randint(bounds[1][0], bounds[1][1]),
        keys[2] : str(random.randint(bounds[2][0], bounds[2][1])) + "s"
    }
    with open(json_file, "w") as out_file:
        json.dump(data, out_file)

# Function returns computation time in case of error returns -1.
def read_json_file(json_file):
	# Load file and validates JSON file structure.
	with open(json_file, "r") as read_file:
		data = json.load(read_file)	
		data_keys = set(data.keys())
		
		# If validation of keys is okay return Time of computation.
		if data_keys == set(keys):
			for i in range(len(keys)):
				check = within_bounds(data[keys[i]], bounds[i][0], bounds[i][1], is_time[i])
				if check != "OK":
					error_message = "ERROR at key: " + keys[i] + "\n " + check
					return error(error_message)	
			
			return int(data[keys[2]][:-1]) 
		else:
			return error("Keys don't match.")
