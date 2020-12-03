from xml.etree import ElementTree as ET

p = ET.Element('parent')
p.text = "Big boss - parent!"

c1 = ET.SubElement(p, 'child_1')
c1.text = f'This is first child of {p.tag}'

d1 = ET.SubElement(c1, 'next_level_1')

c2 = ET.SubElement(p, 'child_2')
c2.text = f'This is second child of {p.tag}'

d2 = ET.SubElement(c2, 'next_level_for_c2')

ET.dump(p)

my_tree = ET.ElementTree(p)
my_tree.write('27.created_little_tree.xml')

root = my_tree.getroot()
#print(root.text)

for e in root:
    print(e.tag, ' ', e.text)