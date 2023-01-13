# Set a variable birthday = "1-May-12".


# Parse the date using datetime.datetime.strptime.

# Use strftime to output a date that looks like "5/1/2012".
from datetime import datetime

birthday = "1-May-12"
date_format = "%d-%B-%y"

parsed_date = datetime.strptime(birthday, date_format)
date_str = parsed_date.strftime("%-m/%-d/%Y") # 01/11/17
print(date_str)
