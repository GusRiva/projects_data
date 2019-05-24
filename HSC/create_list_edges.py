import codecs
import json
import csv
import pandas
import itertools

#Open the list of manuscripts with works
with codecs.open("list_manuscripts_with_works.json", "r", "utf-8") as source:
	list_manuscripts = json.load(source)

#Open the list of nodes (works)
with codecs.open("list_nodes_slim.csv", "r", "utf-8") as source:
	list_nodes_slim = pandas.read_csv(source)



#Create the new file, list of edges
with codecs.open("list_edges.csv", "w", "utf-8") as output:
	#  Write the table header
	filewriter = csv.writer(output, delimiter = ",")
	filewriter.writerow(['Source','Target','Type'])

	#Write the data
	for manuscript in list_manuscripts:
		works_in_manuscript = list_manuscripts[manuscript]
		#itertools.combinations creates all the combinations of range two possibles
		if len(works_in_manuscript) > 1:
			for subset in itertools.combinations(works_in_manuscript, 2):
				filewriter.writerow([subset[0],subset[1],'undirected'])
			






