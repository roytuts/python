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

#import csv

#with open('sample.csv', newline='') as csvfile:
#	reader = csv.DictReader(csvfile)
#	for row in reader:
#		print(row['policyID'], row['statecode'], row['county'])

from io import StringIO
import csv

string = """policyID,statecode,county,eq_site_limit,hu_site_limit,fl_site_limit,fr_site_limit,tiv_2011,tiv_2012,eq_site_deductible,hu_site_deductible,fl_site_deductible,fr_site_deductible,point_latitude,point_longitude,line,construction,point_granularity
119736,FL,CLAY COUNTY,498960,498960,498960,498960,498960,792148.9,0,9979.2,0,0,30.102261,-81.711777,Residential,Masonry,1
448094,FL,CLAY COUNTY,1322376.3,1322376.3,1322376.3,1322376.3,1322376.3,1438163.57,0,0,0,0,30.063936,-81.707664,Residential,Masonry,3
206893,FL,CLAY COUNTY,190724.4,190724.4,190724.4,190724.4,190724.4,192476.78,0,0,0,0,30.089579,-81.700455,Residential,Wood,1
333743,FL,CLAY COUNTY,0,79520.76,0,0,79520.76,86854.48,0,0,0,0,30.063236,-81.707703,Residential,Wood,3
172534,FL,CLAY COUNTY,0,254281.5,0,254281.5,254281.5,246144.49,0,0,0,0,30.060614,-81.702675,Residential,Wood,1
785275,FL,CLAY COUNTY,0,515035.62,0,0,515035.62,884419.17,0,0,0,0,30.063236,-81.707703,Residential,Masonry,3
995932,FL,CLAY COUNTY,0,19260000,0,0,19260000,20610000,0,0,0,0,30.102226,-81.713882,Commercial,Reinforced Concrete,1
223488,FL,CLAY COUNTY,328500,328500,328500,328500,328500,348374.25,0,16425,0,0,30.102217,-81.707146,Residential,Wood,1
433512,FL,CLAY COUNTY,315000,315000,315000,315000,315000,265821.57,0,15750,0,0,30.118774,-81.704613,Residential,Wood,1"""

f = StringIO(string)
reader = csv.reader(f, delimiter=',')
for row in reader:
    print(','.join(row))
