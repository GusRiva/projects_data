import codecs
import json
import csv

#Read the json file
with codecs.open("handschriftencensus_data.json", "r", "utf-8") as source:
	data = json.load(source)

set_manuscripts = set([])

for elem in data:
	if 'manuscripts' in data[elem].keys():
		for manuscript in data[elem]['manuscripts']:
			set_manuscripts.add(manuscript)


list_manuscripts = list(set_manuscripts)
#The len of list_manuscripts is 16352

manuscripts_json = json.dumps(list_manuscripts)



with codecs.open("list_manuscripts.json", "w", "utf-8") as file:
	file.write(manuscripts_json)



