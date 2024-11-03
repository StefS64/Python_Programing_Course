import os

from csv_write_and_read import write_csv_file, read_csv_file
from json_write_and_read import write_json_file, read_json_file

# List of day abbreviations (shortened days of the week)
DAYS_SHORT = ['pn', 'wt', 'śr', 'cz', 'pt', 'sb', 'nd']
# List of full names of the days of the week
DAYS_FULL = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']


def expand_day_range(day_range):
    # If the input is a range, e.g., pn-śr or śr-pn
    if '-' in day_range:
        # Split the input range into start and end days
        start, end = day_range.split('-')
        # Find the index of the start and end days in the shortened list
        start_idx = DAYS_SHORT.index(start)
        end_idx = DAYS_SHORT.index(end)

        # Case 1: Normal range, e.g., pn-śr
        if start_idx <= end_idx:
            # Return the days between the start and end, inclusive
            return DAYS_FULL[start_idx:end_idx + 1]
        else:
            # Case 2: The range wraps around the end of the week, e.g., śr-pn
            return DAYS_FULL[start_idx:] + DAYS_FULL[:end_idx + 1]
    else:
        # If it's a single day, return the corresponding full name
        return [DAYS_FULL[DAYS_SHORT.index(day_range)]]

def changing_times_of_day(lst):
    new_list = []
    for element in lst:
        if element == 'r':
            new_list.append('rano')
        elif element == 'w':
            new_list.append('wieczorem')
        else:
            print("Nieprawidłowa pora dnia!")
    return new_list

def generate_directory_structure(selected_months, selected_days, times_of_day, write, csv):
    time_of_computation = 0
    times_of_day_index = 0
    # Generate the full times of day list
    times_of_day_list = changing_times_of_day(times_of_day)
    # Check if the lengths of months and days lists are the same
    if len(selected_months) == len(selected_days):
        for i in range(len(selected_months)):
            # Ensure selected_days has enough entries
            if i < len(selected_days):
                days = expand_day_range(selected_days[i])
                for j in range(len(days)):
                    # Construct the directory path based on current month, day, and time of day
                    if times_of_day_index < len(times_of_day_list):
                        dir_path = os.path.join('.', selected_months[i], days[j], times_of_day_list[times_of_day_index])
                        times_of_day_index += 1
                    else:
                        # Default to 'rano' if no more time of day entries are available
                        dir_path = os.path.join('.', selected_months[i], days[j], 'rano')

                    if write:
                        os.makedirs(dir_path, exist_ok=True)
                        if csv:
                            file_path = os.path.join(dir_path, 'dane.csv')
                            with open(file_path, 'w', newline='') as csvfile:
                                pass
                            write_csv_file(file_path)
                        else:
                            file_path = os.path.join(dir_path, 'dane.json')
                            with open(file_path, 'w', newline='') as jsonfile:
                                pass
                            write_json_file(file_path)
                    else:
                        if csv:
                            file_path = os.path.join(dir_path, 'dane.csv')
                            time_of_computation += read_csv_file(file_path)
                        else:
                            file_path = os.path.join(dir_path, 'dane.json')
                            time_of_computation += read_json_file(file_path)

        if not write :
            print("Time of computation: " + str(time_of_computation))

    else:
        print("Nieprawidłowa liczba argumentów!")
