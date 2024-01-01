import csv

csv_path = "./test.csv"
with open(csv_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
      print(row)
