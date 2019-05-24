import codecs
import json
import csv

#Creates the list of nodes in csv from the handschriftencensus.json file, which has this structure:
#dict = {Id:{"title":"foo","manuscripts": [A,B,C]}}
#Outputs a file "list_nodes.csv"

#Read the json file
with codecs.open("handschriftencensus_data.json", "r", "utf-8") as source:
	data = json.load(source)

with codecs.open("list_nodes.csv", "w", "utf-8") as output:
	filewriter = csv.writer(output, delimiter = ",")
	filewriter.writerow(['Id','Label','Rating'])

	for elem in data:
		#Only write works with witnesses
		if 'manuscripts' in data[elem].keys():
			filewriter.writerow([int(elem),data[elem]['title'],len(data[elem]['manuscripts'])])




