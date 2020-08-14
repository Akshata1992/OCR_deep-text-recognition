#Import XML library ElementTree
import xml.etree.ElementTree as ET
import os

#parse the XML file
path = 'E:/LincodeLabs/batch_48/batch_48'
data = None
for filename in os.listdir(path):
    if filename.endswith('.xml'):
        fullname  = os.path.join(path,filename)
        file = ET.parse(fullname)
        root = file.getroot()

for i in root:
    if data is None:
        data = root
    else:
        lookfor = root.findall('object')
        for object in lookfor:
            data.append(object)
            file.write(path + '/mergedXML.xml')
