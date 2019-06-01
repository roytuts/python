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

#root element
root = ET.Element('bookstore', {'specialty':'novel'})

#book sub-element
book = ET.SubElement(root, 'book', {'style':'autobiography'})

author = ET.SubElement(book, 'author')

firstName = ET.SubElement(author, 'first-name')
firstName.text = 'Joe'

lastName = ET.SubElement(author, 'last-name')
lastName.text = 'Bob'

award = ET.SubElement(author, 'award')
award.text = 'Trenton Literary Review Honorable Mention'

price = ET.SubElement(book, 'price')
price.text = str(12)

#magazine sub-element
magazine = ET.SubElement(root, 'magazine', {'style':'glossy', 'frequency':'monthly'})

price = ET.SubElement(magazine, 'price')
price.text = str(12)

subscription = ET.SubElement(magazine, 'subscription', {'price':'24', 'per':'year'})

#write to file
tree = ET.ElementTree(indent(root))
tree.write('bookstore2.xml', xml_declaration=True, encoding='utf-8')