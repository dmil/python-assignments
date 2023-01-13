# load a python package
import json

# open a file and read it
with open('friends.json', 'r') as f:

    # save the contents of the 
    # file in data variable
    data = json.load(f)
    
print(data)













# # loading a python package
# import json

# rows = [
#     {"name": "Rachel", "age": True},
#     {"name": "Monica", "age": 34},
#     {"name": "Phoebe", "age": 37}
# ]

# with open('friends.json', 'w') as f:
#     json.dump(rows, f)
