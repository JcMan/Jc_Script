# -*-coding:utf-8 -*-
#  python 2.7
import os
import sys
import PIL.Image as Image

def changeAll():
    path = os.getcwd()
    files = os.listdir(path)
    result = os.path.join(path,'result')
    if not os.path.exists(result):
        os.mkdir(result)
    for file in files:
        if file.lower().endswith('png') or file.lower().endswith('jpg'):
            filepath = os.path.join(path,file)
            filetype = os.path.splitext(filepath)[1].replace('.','').upper()
            if filetype == 'JPG':
                filetype = 'JPEG'
            img = Image.open(filepath)
            scale = float(sys.argv[1])
            width = int(img.size[0]*scale)
            height = int(img.size[1]*scale)
            img = img.resize((width,height),Image.ANTIALIAS)
            img.save(os.path.join(result,file),filetype,quality = 99)
            print(file+' changed!')


def changeOne():
    path = os.getcwd()
    filepath = os.path.join(path,sys.argv[1])
    result = os.path.join(path,'result')
    if not os.path.exists(filepath):
        print(sys.argv[1]+' not exist!')
    else:
        filetype = os.path.splitext(filepath)[1].replace('.','').upper()
        if filetype == 'JPG':
            filetype = 'JPEG'
        result = os.path.join(path,'result')
        if not os.path.exists(result):
            os.mkdir(result)
        img = Image.open(filepath)
        scale = float(sys.argv[2])
        width = int(img.size[0]*scale)
        height = int(img.size[1]*scale)
        img = img.resize((width,height),Image.ANTIALIAS)
        img.save(os.path.join(result,sys.argv[1]),filetype,quality = 99)
        print(sys.argv[1]+' changed!')


if __name__ == '__main__':
    if len(sys.argv)==2:
        changeAll()
    else:
        changeOne()
