import csv
import json

csv_path = "./test.csv"
json_path = "./test.json"

with open(json_path, 'w', encoding='utf-8') as jsonf:
    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            json.dump(row, jsonf)
            jsonf.write('\n')
