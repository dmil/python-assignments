person = {
	"firstname": "Dhrumil",
	"lastname": "Mehta",
	"title": "Prof",
	"classes": ["section a", "section b"],
	"students": [
		{
			"firstname": "jacob",
			"lastname": "jameson",
			"gender": "m"
		},
		{
			"firstname": "patrick",
			"lastname": "song",
			"gender": "m"
		}
	]
}

# print(person["students"][0]["gender"])
for item in person["students"]:
	if item["gender"] == "m":
		print(item)



