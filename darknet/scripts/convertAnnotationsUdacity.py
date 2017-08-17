import csv
from os import listdir, getcwd, walk
import pickle
import os
from os.path import join


classes = ["car"]
textPath="labels/"
annotationsPath="annotations/"

# Size is a tuple of [width, height]
# Box is a list containing [xmin, ymin, xmax, ymax]
def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[2])/2.0
    y = (box[1] + box[3])/2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convertAnnotations(image_id, W, H):
    cl=[]
    coord=[]
    b=()
    out_file = open('labels/%s.txt'%(image_id), 'w')

    with open('udacity.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='"')
        for row in spamreader:
            if row[0]==image_id:
                for i in range(0,len(row)/5):
                    c= int(row[(i*5)+5])
                    if c not in [1, 2, 3, 4]:
                        cl.append(c)
                        coord.append((row[i*5+1],row[i*5+2],row[i*5+3],row[i*5+4]))
                    else:
                        continue

        for i in range(0,len(cl)):
            b=(coord[i][0], coord[i][1], coord[i][2], coord[i][3])
            w=int(coord[i][1])-int(coord[i][0])
            h=int(coord[i][3])-int(coord[i][2])
            if cl[i] == 0:
                out_file.write("0 \n" + " ".join([str(a) for a in b]) +'\n')
##            elif cl[i]==2:
##                out_file.write("1 \n" + " ".join([str(a) for a in b]) +'\n')
            else:
                continue

def writeConversions():
    width = 1920
    height= 1080
    wd = getcwd()
    if not os.path.exists('labels/'):
        os.makedirs('labels/')
    list_file = open('train.list', 'w')
    print "Conversion Started!"
    with open('udacity.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ',quotechar='"')
        for row in reader:
            list_file.write('%s/JPEGImages/%s\n'%(wd, row[0]))
            convertAnnotations(row[0],width, height)
        list_file.close()
    print "Finished conversion from csv!"

def convertToDarknet():

    if not os.path.exists('annotations/'):
        os.makedirs('annotations/')
    print "Started converting to darknet annotations!"
    txt_name_list = []
    for (dirpath, dirnames, filenames) in walk(textPath):
        txt_name_list.extend(filenames)
        break
    #print(txt_name_list)

    for txt_name in txt_name_list:
        """ Open input text files """
        txt_path = textPath + txt_name
        txt_file = open(txt_path, "r")
        lines = txt_file.read().split('\n')   #for ubuntu, use "\r\n" instead of "\n"
        """ Open output text files """
        txt_outpath = annotationsPath + txt_name
        txt_outfile = open(txt_outpath, "w")

        """ Convert the data to YOLO format """
        cls_id=0
        for line in lines:
            if(len(line) > 2):
                elems = line.split(' ')
                xmin = elems[0]
                ymin = elems[1]
                xmax = elems[2]
                ymax = elems[3]
                w= 1920
                h= 1080
                b = (float(xmin), float(ymin), float(xmax), float(ymax))
                bb = convert((w,h), b)
                txt_outfile.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
            else:
                cls_id=line
    print "Finished conversion to darknet!"

def main():
    writeConversions()
    convertToDarknet()

main()
