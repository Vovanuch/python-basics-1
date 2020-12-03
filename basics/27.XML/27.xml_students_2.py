from xml.etree import ElementTree

my_tree = ElementTree.parse("27.students.xml")
for elem in my_tree.iter():
    print(elem.tag, ' ', elem.text)
    
for elem in my_tree.iter():
   if elem.text == 'Ivanov':
       elem.text = 'Kuznetcov'
       print(elem.text)

my_tree.write("27.students_copy.xml")