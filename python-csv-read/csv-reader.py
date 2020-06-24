#import csv

#with open('sample.csv', newline='') as csvfile:
#	samplereader = csv.reader(csvfile, delimiter=',', quotechar='|')
	
#	for row in samplereader:
#		print(', '.join(row))

#file = open('sample.csv')
#csv_file = csv.reader(file)   
#data = []

#for row in csv_file: 
	#data.append(row)

#file.close()

#print (data[1:])

#with open('sample.csv', newline='') as f:
#    reader = csv.reader(f)
#    for row in reader:
#        print(row)

#import csv, sys

#filename = 'sample.csv'
#with open(filename, newline='') as f:
#    reader = csv.reader(f)
#    try:
#        for row in reader:
#            print(row)
#    except csv.Error as e:
#        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

#import csv

#with open('sample.csv', newline='', encoding='utf-8') as f:
#    reader = csv.reader(f)
#    for row in reader:
#        print(row)

#import csv

#with open('sample', newline='') as f:
#    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
#    for row in reader:
#        print(row)

import csv

with open('sample.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['policyID'], row['statecode'], row['county'])