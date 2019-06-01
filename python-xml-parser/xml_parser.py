import xml.etree.ElementTree as ET

tree = ET.parse('bookstore.xml')
root = tree.getroot()

for child in root:
	print(child.tag, child.attrib)
	for node in child:
		print(node.tag, node.attrib, node.text)
		for c in node:
			print(c.tag, c.attrib, c.text)