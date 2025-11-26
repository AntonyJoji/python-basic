data='''<?xml version="1.0" encoding="UTF-8"?>
<metadata>
<food>
    <item name="breakfast">idly</item>
    <price>$2.5</price>
    <description>
    Two idly's with chutney
    </description>
    <calories>553</calories>
</food>

<food>
    <item name="breakfast">Dosa</item>
    <price>$1.5</price>
    <description>
    Dosa with vada
    </description>
    <calories>700</calories>
</food>
</metadata>'''


import xml.etree.ElementTree as ET

# tree = ET.fromstring(data)
# print(tree)
# print (tree.tag)
# print(tree[0].tag)
# print(tree[0][1].tag)

# for i in tree:
#     print(i.tag)

# for i in tree[0]:
#     print(i.tag)




# tree = ET.parse('sample.xml')
# print(tree)
# mytree = tree.getroot()
# print(mytree)
# print(mytree[0].tag)
# print(mytree[0][0].tag)


# for i in mytree:
#     print(i.tag)

# for i in mytree[0]:
#     print(i.tag)


# for i in  mytree[0]:
#     print(i.tag,i.attrib)



# xml ='''
# <root>
#     <item>one</item>
#     <item>two</item>
#     <pro>
#         <item>three</item>
#     </pro>
# </root>


# '''

# tree =ET.fromstring(xml)
# print([val.text for val in tree.findall('item')])
# print([val.text for val in tree.iter('item')])



tree = ET.parse('sample.xml')
mytree =tree.getroot()

# for i in mytree.findall('book'):
#     auth =i.find('author').text
#     title =i.find('title').text
#     print(auth,title)

# #### adding new discrition
# for i in mytree.iter('discription'):
#     a=str(i.text)+'new data has been added'
#     i.text =a
# tree.write('new.xml')



# for i in mytree.iter('discription'):
#     a=str(i.text)+'new data has been added'
#     i.text =a
#     i.set('update','yes')
# tree.write('new1.xml')

#### specific update
# for i in mytree[0].iter('discription'):
#     a=str(i.text)+'new data has been added'
#     i.text =a
#     i.set('update','yes')
# tree.write('new1.xml')


#### to sreate new element
# ET.SubElement(mytree,'speciality')
# for i in mytree.iter('speciality'):
#     i.text = 'south indian food'
# tree.write('new3.xml')

### inside the catlog 0th index
# ET.SubElement(mytree[0],'speciality')
# for i in mytree.iter('speciality'):
#     i.text = 'south indian food'
# tree.write('new4.xml')

#### on every tag to create

# for i in range(len(mytree)):
#     ET.SubElement(mytree[i],'speciality')
#     for i in mytree.iter('speciality'):
#         i.text ='south indian food'
# tree.write('new5.xml')

#######or

# for i in mytree.iter('book'):
#     val=ET.SubElement(i,'speciality')
#     val.text= 'south indian book'
# tree.write('new6.xml')


### to delete the attribute
# tree = ET.parse('new6.xml')
# mytree = tree.getroot()

# mytree[0].attrib.pop('id')
# tree.write('new7.xml')

# mytree[0].remove(mytree[0][0])
# tree.write('new8.xml')

# mytree[0].clear()
# tree.write('new9.xml')