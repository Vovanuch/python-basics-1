import csv

with open("students.csv", "r") as f:
    reader = csv.reader(f, )
    for row in reader:
        print(row)