import csv

stud_append = [["Joe", "Dastin", 70, "Good job, Joe!"],
               ['Mary', 'Christand', 92, "Excellent!"]
]

stud_append_2 = [["Kate", "Adder", 45, "Not good..."],
               ['Liza', 'Coudrow', 56, "So-so."]
]

def print_from_csv_file(filename, mode):
    with open(filename, mode) as f:
        print("Current file:")
        reader = csv.reader(f)
        for r in reader:
            print(r)    
    
def write_to_csv_file(filename, mode, structure):
    ''' How to write and read after it'''
    with open(filename, mode) as f:
        writer = csv.writer(f)
        for stud in stud_append:
            writer.writerow(stud)

def write_to_csv_file_2(filename, mode, structure):
    ''' How to write and read after it'''
    with open(filename, mode) as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC) # csv.QUOTE_ALL or csv.QUOTE_NONNUMERIC or csv.QUOTE_NONE
        writer.writerows(structure)
    

print_from_csv_file("students.csv", "r")

write_to_csv_file("students.csv", "a", stud_append)
        
print_from_csv_file("students.csv", "r")

write_to_csv_file_2("students.csv", "a", stud_append_2)
        
print_from_csv_file("students.csv", "r")