import xml.etree.ElementTree as ET

#pretty print method
def indent(elem, level=0):
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem
	
tree = ET.parse('bookstore2.xml')
root = tree.getroot()

#update all price
for price in root.iter('price'):
	new_price = int(price.text) + 5
	price.text = str(new_price)
	price.set('updated', 'yes')
	
#write to file
tree = ET.ElementTree(indent(root))
tree.write('bookstore2.xml', xml_declaration=True, encoding='utf-8')