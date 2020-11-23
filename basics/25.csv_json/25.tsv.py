import csv

with open("students2.tsv", "r") as inf:
    text = csv.reader(inf, delimiter="\t")
    for line in text:
        print(line)