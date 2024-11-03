import csv
import random
import sys


# Initialize keys and ranges of data.
keys = ['Model', 'Output value', 'Time of computation']
ranges = [['A', 'C'], [0, 1000], [0, 1000]]


# Check whether the data row is correct or not. Return tuple (boolean, string): (True, "") if the data row is correct, (False, error_comment) otherwise.
def check_data(row):
    for i in range(len(keys)):
        value = row[keys[i]]
        if keys[i] == 'Time of computation':
            if row[keys[i]][-1] == 's':
                value = int(row[keys[i]][:-1])
            else:
                error_comment = f"Incorrect format of value of '{keys[i]}'. Expected [number]s. Got {value}."
                return (False, error_comment)
        elif keys[i] == 'Output value':
            value = int(value)
                
        if type(value) != type(ranges[i][0]):
            error_comment = f"Incorrect type of value of '{keys[i]}'. Expected type {type(ranges[i][0])}. Got {type(value)}."
            return (False, error_comment)
        if not ranges[i][0] <= value <= ranges[i][1]:
            error_comment = f"Incorrect value of '{keys[i]}'. Expected value in range {ranges[i][0]}-{ranges[i][1]}. Got {value}."
            return (False, error_comment)
            
    return (True, "")


def write_csv_file(csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys, delimiter=';')
        writer.writeheader();
        writer.writerow({
            keys[0]: chr(random.randint(ord(ranges[0][0]), ord(ranges[0][1]))),
            keys[1]: random.randint(ranges[1][0], ranges[1][1]),
            keys[2]: str(random.randint(ranges[2][0], ranges[2][1])) + 's'
        })


# Return time of computation if the model is A, 0 otherwise.
def read_csv_file(csv_file):
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        if (reader.fieldnames == keys):
            row = next(reader)
            feedback = check_data(row)
            if feedback[0]:
                if row['Model'] == 'A':
                    return int(row['Time of computation'][:-1])
                else:
                    return 0
            else:
                error(feedback[1])
        else:
            error("Keys don't match.")


def error(comment):
    print("INVALID FILE DATA!", comment, sep='\n')
    sys.exit(-1)
