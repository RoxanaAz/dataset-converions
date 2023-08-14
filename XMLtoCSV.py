import os
import xml.etree.cElementTree as ET
import xml.dom.minidom as mini
import json
#def mydatasetloader(name, thing_classes):

data=[]

file_name=[]
image_id=[]
heigthImg=[]
widthImG=[]
category_id=[]
bbox=[]
bbox_mode=[]

MydatasetimagePath="C:\\Mine\\University\\dissertation\\code\\environment\\gpu\\pytorch_custom_object_detection\\myDataset\\train\\"
MydatasetannotationPath="C:\\Mine\\University\\dissertation\\code\\environment\\gpu\\pytorch_custom_object_detection\\myDataset\\train_labels.csv"
f = open(MydatasetannotationPath)
trainlines = f.readlines()
f.close()

imagePath="C:\\Mine\\University\\dissertation\\code\\environment\\fewShot_object_detection\\few-shot-object-detection\\datasets\\VOCtrainval_25-May-2011\\TrainVal\\VOCdevkit\\VOC2011\\JPEGImages\\"
annotationPath="C:\\Mine\\University\\dissertation\\code\\environment\\fewShot_object_detection\\few-shot-object-detection\\datasets\\VOCtrainval_25-May-2011\\TrainVal\\VOCdevkit\\VOC2011\\Annotations\\"
allfiles=os.listdir(annotationPath)

ID2CLASS = {
        1: "person",
        2: "bicycle",
        3: "car",
        4: "motorcycle",
        5: "aeroplane",
        6: "bus",
        7: "train",
        8: "truck",
        9: "boat",
        10: "traffic light",
        11: "fire hydrant",
        13: "stop sign",
        14: "parking meter",
        15: "bench",
        16: "bird",
        17: "cat",
        18: "dog",
        19: "horse",
        20: "sheep",
        21: "cow",
        22: "elephant",
        23: "bear",
        24: "zebra",
        25: "giraffe",
        27: "backpack",
        28: "umbrella",
        31: "handbag",
        32: "tie",
        33: "suitcase",
        34: "frisbee",
        35: "skis",
        36: "snowboard",
        37: "sports ball",
        38: "kite",
        39: "baseball bat",
        40: "baseball glove",
        41: "skateboard",
        42: "surfboard",
        43: "tennis racket",
        44: "bottle",
        46: "wine glass",
        47: "cup",
        48: "fork",
        49: "knife",
        50: "spoon",
        51: "bowl",
        52: "banana",
        53: "apple",
        54: "sandwich",
        55: "orange",
        56: "broccoli",
        57: "carrot",
        58: "hot dog",
        59: "pizza",
        60: "donut",
        61: "cake",
        62: "chair",
        63: "couch",
        64: "pottedplant",
        65: "bed",
        67: "diningtable",
        70: "toilet",
        72: "tvmonitor",
        73: "laptop",
        74: "mouse",
        75: "remote",
        76: "keyboard",
        77: "cell phone",
        78: "microwave",
        79: "oven",
        80: "toaster",
        81: "sink",
        82: "refrigerator",
        84: "book",
        85: "clock",
        86: "vase",
        87: "scissors",
        88: "teddy bear",
        89: "hair drier",
        90: "toothbrush",
        91: "SafetyVest",
        92: "helmet"

    }
CLASS2ID = {v: k for k, v in ID2CLASS.items()}
anno = {i: [] for i in ID2CLASS.keys()}


for i in allfiles:
    tree=ET.parse(annotationPath+i)
    dataset=tree.getroot()
    
    XMLdoc=mini.parse(annotationPath+i)
    size=XMLdoc.getElementsByTagName('size')
    for lenn in size:
        width=lenn.getElementsByTagName('width')[0].childNodes[0].data
        heigth=lenn.getElementsByTagName('height')[0].childNodes[0].data
    object=XMLdoc.getElementsByTagName('object')
    imageName=XMLdoc.getElementsByTagName('filename')[0].childNodes[0].data

    #print('new', imageName, width, heigth)
    for file in object:
        #file1=file.tag
        class_name=file.getElementsByTagName('name')[0].childNodes[0].data
        #print('label',imageID)
        xmin=file.getElementsByTagName('xmin')[0].childNodes[0].data
        #print('xmin',xmin)
        xmax=file.getElementsByTagName('xmax')[0].childNodes[0].data
        #print('xmax',xmax)
        ymin=file.getElementsByTagName('ymin')[0].childNodes[0].data
        #print('ymin',ymin)
        ymax=file.getElementsByTagName('ymax')[0].childNodes[0].data
        #print('ymax',ymax)
        
        #print(anno)
        #print(ID2CLASS[1])
        if class_name=="motorbike": class_name="motorcycle"
        if class_name=="sofa": class_name="couch"

        imageID=CLASS2ID[str(class_name)]
        #print(imageID)
       
        annotation = {"file_name" : imagePath+imageName, 
                      "image_id" :class_name,
                      "height" :heigth,
                      "width" : width,
                      "annotations":{
                          "category_id" :imageID,
                          "bbox" : [xmin, ymin, xmax, ymax],
                          #"bbox_mode" : BoxMode.XYXY_ABS,
                      }}
        
        # file_name.append(imagePath+imageName) # full path to image
        # image_id.append(class_name) # image unique ID
        # widthImG.append(width) # height of image
        # heigthImg.append(heigth) # width of image
        # #annotations: []
        # category_id.append(imageID)#thing_classes.index("class_name"), # class unique ID
        # bbox.append([xmin, ymin, xmax, ymax]) # bbox coordinates
        # bbox_mode.append("BoxMode.XYXY_ABS") # bbox mode, depending on your format
        data.append(annotation)
    
#print(data)
for i in range(1,len(trainlines)):

    states=trainlines[i][:len(trainlines[i])-1].split(",")
    print('states',states)
    #print('image_check',image_check)
    
    class_name=states[3]
    name=states[0]
    xmin = int(states[4])
    ymin = int(states[5])
    xmax = int(states[6])
    ymax = int(states[7])
    width= int(states[1])
    heigth=int(states[2])
    
    imageID=CLASS2ID[str(class_name)]

    annotation = {"file_name" : MydatasetimagePath+name, 
                    "image_id" :class_name,
                    "height" :heigth,
                    "width" : width,
                    "annotations":{
                        "category_id" :imageID,
                        "bbox" : [xmin, ymin, xmax, ymax],
                        #"bbox_mode" : BoxMode.XYXY_ABS,
                    }}
    data.append(annotation)
print(data)
with open("sample.json", "w") as outfile:
    json.dump(data, outfile)
    
#    return data

