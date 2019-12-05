import xml.etree.ElementTree as ET

tree = ET.parse('C:\\Users\\Girish\\Desktop\\person.xml')
root = tree.getroot()

for person in root.findall('person'):
    for promoter in person.findall('promoter'):
        if promoter.find('lastname').text == 'Eddleberry':
            print('I found:', promoter.find('lastname').text)
