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




tree = ET.parse('sample.xml')
print(tree)
mytree = tree.getroot()
print(mytree)
print(mytree[0].tag)
print(mytree[0][0].tag)


for i in mytree:
    print(i.tag)

for i in mytree[0]:
    print(i.tag)


for i in  mytree[0]:
    print(i.tag,i.attrib)