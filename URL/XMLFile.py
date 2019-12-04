import xml.etree.ElementTree as ET

tree = ET.parse('C:\\Users\\Girish\\Desktop\\person.xml')
root = tree.getroot()

for person in root.findall('person'):
    id = person.get('id')
    name = person.find('name').text
    if name == "Charlie":
        print("ID is: ", id)
