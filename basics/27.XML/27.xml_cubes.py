'''

Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Пример:

<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>

 

Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.

Sample Input:

<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>

Sample Output:

4 3 1

'''

from xml.etree import ElementTree as ET


def go_into(elem, dict_of_elems, level=1):
    # go thru all elements and create dictionary of colors and values 
    #print(elem.attrib, level)
    k = elem.attrib[str(*list(elem.attrib))]
    
    #print(k, level)
    if k in dict_of_elems.keys():
        #print(f'key {k} is exist')
        dict_of_elems[k] += level
    else:
        #print(f'key {k} is NOT exist')
        dict_of_elems[k] = level
    
    if list(elem):
        for i in elem:
            go_into(i, dict_of_elems, level+1)
            
    return dict_of_elems

    
dict_of_elems = dict()
#str_xml = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'#
str_xml = input()

root = ET.fromstring(str_xml)

dict_of_elems = go_into(root, dict_of_elems)

print(dict_of_elems['red'], dict_of_elems['green'], dict_of_elems['blue'])

#print(dict_of_elems)
#ch = list(root)
#print(ch) #.getchildren()
#print(ch.items())

#for i in root:
    


#print(root.tag, root.attrib)

#for child in root:
#    print(child.tag, child.attrib)
   
#dict_cubes[root.tag] = root.attrib
#dict_cubes = add_cube_to_dict(root, dict_cubes)

'''
for elem in root:
    dict_cubes = add_cube_to_dict(elem, dict_cubes)
    
print(dict_cubes)
'''