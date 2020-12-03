from xml.etree import ElementTree

tree = ElementTree.parse("27.students.xml")

root = tree.getroot()
print(root)
print(f'Root element of our tree is {root.tag} with attibutes {root.attrib}')
childs = list(root.getchildren())
print(f'Childs are {childs}')
for ch in childs:
    print(ch.tag, ch.attrib)

print()
for ch in root:
    print(ch.tag, ch.attrib)

print(f'Attribute: {root[0][0].tag}, value: {root[0][0].text}')

for child in root.iter('scores'):
    #print(child)
    score_num = 0
    for s in child:
        score_num += float(s.text)
    print(score_num)
    
    