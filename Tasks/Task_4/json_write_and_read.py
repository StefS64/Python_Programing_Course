from functools import reduce
import json


def contains_exercise():
	print(0)

def change_one_cell(cell):
	if cell['cell_type'] == 'code':
		return "#%%\n" + "".join(cell['source']) + "\n"
	elif cell['cell_type'] == 'markdown':
		return "#%%\n" + "".join(map(lambda line: f"# {line}", cell['source'])) + "\n"
	
def change_ipynb_to_py(json_file):
	with open(json_file, "r") as read_file:
		note = json.load(read_file)
		python_file = json_file.split('.')[0] + ".py"
		print(python_file)
		number_of_exercise = reduce(
		lambda count, cell:count + (1 if cell['cell_type'] == 'markdown' and cell['source'] and "# Ćwiczenie" in cell['source'][0] else 0), note['cells'], 0)
	with open(python_file, 'w') as output:
		print(*list(map(change_one_cell, note['cells'])), file=output)
	print("Number of exercises:" + str(number_of_exercise))

file = input()
change_ipynb_to_py(file)

