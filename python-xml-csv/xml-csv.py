from xml.etree import ElementTree

tree = ElementTree.parse('input.xml')
root = tree.getroot()

data = []

for policy in root:
	policyId = policy.find('policyId').text
	statecode = policy.find('statecode').text
	eq_site_limit = policy.find('eq_site_limit').text
	hu_site_limit = policy.find('hu_site_limit').text
	fl_site_limit = policy.find('fl_site_limit').text
	fr_site_limit = policy.find('fr_site_limit').text
	tiv_2011 = policy.find('tiv_2011').text
	tiv_2012 = policy.find('tiv_2012').text
	eq_site_deductible = policy.find('eq_site_deductible').text
	hu_site_deductible = policy.find('hu_site_deductible').text
	fl_site_deductible = policy.find('fl_site_deductible').text
	fr_site_deductible = policy.find('fr_site_deductible').text
	point_latitude = policy.find('point_latitude').text
	point_longitude = policy.find('point_longitude').text
	line = policy.find('line').text
	construction = policy.find('construction').text
	point_granularity = policy.find('point_granularity').text

	#print('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(policyId, statecode, eq_site_limit, hu_site_limit, fl_site_limit, fr_site_limit, tiv_2011, tiv_2012, eq_site_deductible, hu_site_deductible, fl_site_deductible, fr_site_deductible, point_latitude, point_longitude, line, construction, point_granularity))
	
	data.append('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(policyId, statecode, eq_site_limit, hu_site_limit, fl_site_limit, fr_site_limit, tiv_2011, tiv_2012, eq_site_deductible, hu_site_deductible, fl_site_deductible, fr_site_deductible, point_latitude, point_longitude, line, construction, point_granularity))

print (data)

#with open('output.csv', 'w') as f: f.write('\n'.join([row for row in data[1:]]))