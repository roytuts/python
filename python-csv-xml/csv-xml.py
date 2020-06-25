import csv

f = open('sample.csv')
csv_f = csv.reader(f)   
data = []

for row in csv_f: 
	data.append(row)
f.close()

#print (data[1:])

def convert_row(row):
    return """<policy>
	<policyId>%s</policyId>
    <statecode>%s</statecode>
    <eq_site_limit>%s</eq_site_limit>
    <hu_site_limit>%s</hu_site_limit>
    <fl_site_limit>%s</fl_site_limit>
    <fr_site_limit>%s</fr_site_limit>
    <tiv_2011>%s</tiv_2011>
	<tiv_2012>%s</tiv_2012>
	<eq_site_deductible>%s</eq_site_deductible>
	<hu_site_deductible>%s</hu_site_deductible>
	<fl_site_deductible>%s</fl_site_deductible>
	<fr_site_deductible>%s</fr_site_deductible>
	<point_latitude>%s</point_latitude>
	<point_longitude>%s</point_longitude>
	<line>%s</line>
	<construction>%s</construction>
	<point_granularity>%s</point_granularity>
</policy>""" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16])

print ('\n'.join([convert_row(row) for row in data[1:]]))

with open('output.xml', 'w') as f: f.write('\n'.join([convert_row(row) for row in data[1:]]))