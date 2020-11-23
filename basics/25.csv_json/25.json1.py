import json

student1 = {
    "first_name": "Ivan",
    "last_name": "Petrov",
    "cert": True,
    "scores": [60, 70, 80],
    "description": "Very good!"
}


student2 = {
    "first_name": "Irina",
    "last_name": "Ivanova",
    "cert": False,
    "scores": [65, 75, 55],
    "description": "Not bad!"
}
data = [student1, student2]

# json.dumps creates json-data from python structures
print(json.dumps(data, indent=4, sort_keys=True))

# save data to json-file    
with open("students_3.json", "a") as f:
    json.dump(data, f, indent=4, sort_keys=True)

# save json-data to variable    
data_json = json.dumps(data, indent=4, sort_keys=False)
print('Print from created json-variable/object/text')
print(data_json)

# # load data from json-variable
data_recovered = json.loads(data_json)
print('Data recovered from variable:')
print(data_recovered)

# load data from json-file
data_loaded_from_json_file = ''
with open("students.json", "r") as inf:    # another file!
    data_loaded_from_json_file = json.load(inf)
    print('Data recovered from json-file:')
    print(data_loaded_from_json_file)
    
summ_scores_Ivan = sum(data_loaded_from_json_file[0]['Scores'])
summ_scores_Peter = sum(data_loaded_from_json_file[1]['Scores'])

print('Summ scores, Ivan:', summ_scores_Ivan)
print('Summ scores, Peter:', summ_scores_Peter)