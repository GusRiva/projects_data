import codecs
import json
import csv

#Open the list of manuscripts
with codecs.open("list_manuscripts.json") as source1:
	list_manuscripts = json.load(source1)

#The data in the handschriftencensus_data.json is dict = {Id:{"title":"foo","manuscripts": [A,B,C]}}
with codecs.open("handschriftencensus_data.json") as source2:
	handschriftencensus_data = json.load(source2)

dict_manuscripts_testimonies = {}
#For each manuscript, create a list of all the texts witnessed in the manuscript, using the id of the handschriftencensus_data.json
index = 1 #Just to count on the console
for manuscript in list_manuscripts:
	print(index)
	index = index + 1
	works = []
	for entry in handschriftencensus_data:
		if 'manuscripts' in handschriftencensus_data[entry].keys():
			for testimony in handschriftencensus_data[entry]['manuscripts']:
				if manuscript == testimony:
					works.append(entry)
	dict_manuscripts_testimonies[manuscript] = works
	
	
dict_manuscripts_json = json.dumps(dict_manuscripts_testimonies)

with codecs.open("list_manuscripts_with_works.json","w", "utf-8") as output:
	output.write(dict_manuscripts_json)


