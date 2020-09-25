import json

numbers=[1,3,4,7,9,13,24]

filename="numbers.json"
with open(filename,'w') as f_obj:
    json.dump(numbers, f_obj)
