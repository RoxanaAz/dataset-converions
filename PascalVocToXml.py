import pandas as pd
import numpy as np
from lxml import etree
#import xmlAnnotation.etree.cElementTree as ET
import xml.etree.ElementTree as ET

fields = {'filename', 'width','height','class','xmin', 'ymin', 'xmax', 'ymax'}#]
path="C:\\Mine\\University\\dissertation\\code\\environment\\gpu\\pytorch_custom_object_detection\\myDataset\\validation.csv"
df = pd.read_csv(path, usecols=fields)
print('df', df)

# Change the name of the file.
# This will replace the / with -
def nameChange(x):
    x = x.replace(".jpg", "")
    return x
helmet_num=0
person_num=0
vest_num=0



for i in range(0, len(df)):
    height = df['height'].iloc[i]
    width = df['width'].iloc[i]
    depth = 3

    annotation = ET.Element('annotation')
    ET.SubElement(annotation, 'folder').text = 'JPEGImages'
    ET.SubElement(annotation, 'filename').text = str(df['filename'].iloc[i])
    ET.SubElement(annotation, 'path').text = 'C:\\Mine\\University\\dissertation\\code\\environment\\gpu\\SSD-Tensorflow-On-Custom-Dataset\\VOC2007\\JPEGImages\\'+str(df['filename'].iloc[i])
    source = ET.SubElement(annotation, 'source')
    ET.SubElement(source, 'width').text = 'Unknown'
    size = ET.SubElement(annotation, 'size')
    ET.SubElement(size, 'width').text = str(width)
    ET.SubElement(size, 'height').text = str(height)
    ET.SubElement(size, 'depth').text = str(depth)
    ET.SubElement(annotation, 'segmented').text = '0'
    ob = ET.SubElement(annotation, 'object')
    ET.SubElement(ob, 'name').text = str(df['class'].iloc[i])
    ET.SubElement(ob, 'pose').text = 'Unspecified'
    ET.SubElement(ob, 'truncated').text = '0'
    ET.SubElement(ob, 'difficult').text = '0'
    bbox = ET.SubElement(ob, 'bndbox')
    ET.SubElement(bbox, 'xmin').text = str(df['xmin'].iloc[i])
    ET.SubElement(bbox, 'ymin').text = str(df['ymin'].iloc[i])
    ET.SubElement(bbox, 'xmax').text = str(df['xmax'].iloc[i])
    ET.SubElement(bbox, 'ymax').text = str(df['ymax'].iloc[i])
    
    label=str(df['class'].iloc[i])
    
    print('label',label)
    if label=="helmet":
        helmet_num +=1
    elif label=="person":
        person_num +=1
    elif label=="SafetyVest":
        vest_num +=1

    #df['filename'] = df['filename'].apply(nameChange)
    
    #fileName = str(df['filename'].iloc[i])
    fileName = nameChange(str(df['filename'].iloc[i]))
    tree = ET.ElementTree(annotation)
    ET.indent(tree)
    print('helmet', helmet_num, 'person', person_num, 'vest', vest_num)
    tree.write(fileName + ".xml" ,encoding='utf8')