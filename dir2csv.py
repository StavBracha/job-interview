import argparse
import json
import csv
from pathlib import Path

# Define the arguments that must be passed to the program

parser = argparse.ArgumentParser()
parser.add_argument("path_to_input", type=str, help='Path to input folder required')
parser.add_argument("path_to_output", type=str, help='Path to output folder required')
args = parser.parse_args()

counter = 0
for file in Path(args.path_to_input).glob('*.json'):                     # Find all the json files in the directory
    counter += 1
    with open(file, "r") as patient:                                     # Open the json files and save them as a dict
        data = json.load(patient)
        patient.close()
    if counter == 1:
        field_names = list(data.keys())
        with open(args.path_to_output, 'w') as csvfile:                  # Open a new file and write its headers
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            csvfile.close()
    with open(args.path_to_output, 'a+') as csvfile:                     # Open the existing file and write the data
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writerow(data)

try:
    csvfile.close()
    print('done!')
except NameError:
    print('done!')


