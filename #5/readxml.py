import xml.etree.ElementTree as ET

tree = ET.parse('weather.xml')
root = tree.getroot()

print("//////////////")
for el in range(len(root)):
    for subel in range(len(root[el])):
        print(root[el][subel].text)