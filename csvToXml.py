import csv
import xml.etree.ElementTree as ET
import os
import cv2
#import xml.dom.minidom as mini

path="C:\\Mine\\University\\dissertation\\dataset\\pictor-ppe-20230613T162341Z-001\\backup\\"
image_path="C:\\Mine\\University\\dissertation\\dataset\\pictor-ppe-20230613T162341Z-001\\pictor-ppe\\Images\\"

with open(path+"whole_train_csv.csv" , "r")as file:
    for line in file.readlines():
        xml_name=line.split(".")[0]+'.xml'
        existXMLs = os.listdir('results/')
        name_line=line.split(",")[0]
        xmin_line=line.split(",")[1]
        ymin_line=line.split(",")[2]
        xmax_line=line.split(",")[3]
        ymax_line=line.split(",")[4]
        class_name=line.split(",")[5]
        

        if class_name.split("\n")[0]!='person':
            print('not person',class_name.split("\n")[0])
            

            img=cv2.imread(os.path.join(image_path,name_line))
            h,w,c = img.shape

            text_name=class_name.split("\n")[0]+'.txt'
            #print(text_name)
            with open(text_name, 'a') as f:
                f.write('\n')
                f.write(name_line)


            if xml_name in existXMLs:
                #print('exist',xml_name) 
                #updatfile="/results/" + xml_name
                tree=ET.parse(os.path.join("results" , xml_name))
                
                xmlroot=tree.getroot()
                #child=ET.Element('annotation')
                child2=ET.Element('object')
                name=ET.SubElement(child2,'name')
                pose=ET.SubElement(child2,'pose')
                truncated=ET.SubElement(child2,'truncated')
                difficult=ET.SubElement(child2,'difficult')
                bndbox=ET.SubElement(child2,'bndbox')
                xmin=ET.SubElement(bndbox,'xmin')
                ymin=ET.SubElement(bndbox,'ymin')
                xmax=ET.SubElement(bndbox,'xmax')
                ymax=ET.SubElement(bndbox,'ymax')
                occluded.text='0'
                name.text=class_name.split("\n")[0]
                xmin.text=xmin_line
                ymin.text=ymin_line
                xmax.text=xmax_line
                ymax.text=ymax_line
                xmlroot.append(child2)
                truncated.text='0'
                difficult.text='0'
                occluded.text='0'
                pose.text='Unspecified'
                #tree.append(child2)
                ET.indent(tree)
                #print(os.path.join('results', xml_name))
                tree.write(os.path.join('results', xml_name))
                    



            else:

                #print('Not exist',image_path+name_line)

                anno=ET.Element('annotation')
                folder=ET.SubElement(anno, 'folder')
                filename=ET.SubElement(anno, 'filename')
                source=ET.SubElement(anno, 'source')
                database=ET.SubElement(source, 'database')
                annotation=ET.SubElement(source,'annotation')
                image=ET.SubElement(source,'image')
                size=ET.SubElement(anno,'size')
                width=ET.SubElement(size, 'width')
                height=ET.SubElement(size, 'height')
                depth=ET.SubElement(size, 'depth')
                segmented=ET.SubElement(anno, 'segmented')
                object_name=ET.SubElement(anno,'object')
                name=ET.SubElement(object_name,'name')
                pose=ET.SubElement(object_name,'pose')
                truncated=ET.SubElement(object_name,'truncated')
                difficult=ET.SubElement(object_name,'difficult')
                occluded=ET.SubElement(object_name,'occluded')
                bndbox=ET.SubElement(object_name,'bndbox')
                xmin=ET.SubElement(bndbox,'xmin')
                ymin=ET.SubElement(bndbox,'ymin')
                xmax=ET.SubElement(bndbox,'xmax')
                ymax=ET.SubElement(bndbox,'ymax')
                database.text='The added VOC2007 Database'
                annotation.text='PASCAL VOC2007'
                image.text='pictor-ppe'
                pose.text='Unspecified'
                occluded.text='0'
                database.text='The added VOC2007 Database'
                segmented.text='0'
                name.text=class_name.split("\n")[0]
                filename.text= name_line
                folder.text='VOC2012'
                truncated.text='0'
                difficult.text='0'
                xmin.text=xmin_line
                ymin.text=ymin_line
                xmax.text=xmax_line
                ymax.text=ymax_line
                width.text=str(w)
                height.text=str(h)
                depth.text=str(c)
                #xml_name=line.split(".")[0]+'.xml'
                tree=ET.ElementTree(anno)
                ET.indent(tree)
                #print(os.path.join('results', xml_name))
                tree.write(os.path.join('results', xml_name))
                
        
        
        
        
    
