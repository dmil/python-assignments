import csv
import json

# 1. Read output/vegetables.csv 
#    (see previous section) into a 
#    variable called vegetables.
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)

# 2. Print the variable vegetables.
print(vegetables)

# 3. Write vegetables as a JSON file 
#    called output/vegetables.json. 
with open('vegetables.json', 'w') as f:
    json.dump(vegetables, f)




