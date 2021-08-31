import csv

def save_to_file(db,word):
	name = word
	file = open(f"{word}.csv",mode ="w",encoding="utf8")
	writer = csv.writer(file)
	info = db[word]
	writer.writerow(["local | title | time | pay | reg date"])
	for i in info:
		writer.writerow(list(i.values()))
	return