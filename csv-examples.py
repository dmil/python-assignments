import csv

with open('testwrite.csv', 'r') as f:
    # creates a reader object (kinda like👓)
    reader = csv.DictReader(f)
    rows = list(reader)

print(rows)





















# # import a python package
# import csv

# # open a file
# with open('testwrite.csv', 'w') as f:
#     # create magical writer object
#     pen = csv.writer(f)

#     # use writer to write some rows
#     pen.writerow(['col1', 'col2'])
#     pen.writerow(['val1', 'val2'])
#     pen.writerow(['val1', 'val2'])
#     pen.writerow(['val1', 'val2'])



