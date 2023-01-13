vegetables = [
     {"name": "eggplant", "color": "purple"},
     {"name": "tomato", "color": "red"},
     {"name": "corn", "color": "yellow"},
     {"name": "okra", "color": "green"},
     {"name": "arugula", "color": "green"},
     {"name": "broccoli", "color": "green"}
 ]


# In the loop, write the name of each vegetable 
# and the color into a CSV called vegetables.csv


# load a python package
import csv

# open a file
with open('vegetables.csv', 'w') as f:

    # create a writer
    writer = csv.writer(f)

    # write the header row
    writer.writerow(['name', 'color'])

    # Loops through each vegetable and write the name and color
    for x in vegetables:
        writer.writerow([x["name"], x["color"]])










