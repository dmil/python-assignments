from datetime import datetime

raw_date = "2017-01-11"
date_format = "%Y-%m-%d"

# Parse the raw_date string
parsed_date = datetime.strptime(raw_date, date_format)

# Convert the parsed date back to a string
#  (but in a different format)
date_str = parsed_date.strftime("%m/%d/%y") 

# Print it out
print(date_str)
