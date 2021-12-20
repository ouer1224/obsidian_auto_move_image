#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import shutil
import os
import re


def getfilePath():
    # for i in sys.argv:
    print(f"sys.argv={sys.argv}")
    filename = sys.argv[-1];
    filepath = sys.argv[-2]
    strpath = filepath.split('/')
    filepath = strpath[0]
    print(f'name={filename}, path={filepath}')
    return filename, filepath

def getimagePath(root,infor):
    nameImage=''
    pathImage=''
    tmp=infor.split('/')
    pathImage=root+'\\'+tmp[0]
    nameImage=tmp[1]
    print(f'nameImage={nameImage},pathImage={pathImage}')
    return nameImage,pathImage


def remove_file(old_path, new_path, filename):
    print(old_path)
    print(new_path)

    src = os.path.join(old_path, filename)
    dst = os.path.join(new_path, filename)
    print('src:', src)
    print('dst:', dst)
    shutil.move(src, dst)

def checkIsImagelink(root,s):
    res = '!\[\[(.*?)\]\]'
    result = re.search(res, s);
    print(f's={s}')
    print(result)
    nameImage=''
    pathImage=''
    if(result==None):
        return None,None;
    else:
        print(result);
        tmp=result.group(1);
        print(f"tmp={tmp}")
        tmp=tmp.split('/')
        pathImage=root+'\\'+tmp[0]
        nameImage=tmp[1]
        return nameImage,pathImage

def moveImageToDest(imagePath, new_note_path, filename):
    tmp=imagePath.split('\\')
    tmp=tmp[-1]
    new_path=new_note_path+'\\'+tmp;
    remove_file(imagePath, new_path, filename);





if __name__ == '__main__':
    # 记录当前文件的路径到log.txt中, 第一行是source, 第二行是dest.
    # filename, filepath=getfilePath()
    filepath=r'D:\note_base\obsidian'
    filename=r'test.md'
    newpath=filepath+'.\\life'
    new_path_note = newpath;
    print(f'filename={filename}, path={filepath}')
    logname=r'D:\note_base\obsidian\log.txt'
    strall = ''
    lines=[]
    with open(filepath+'\\'+filename, 'r+',encoding='utf-8') as fp:
        lines=fp.readlines()
        print(f'lines={lines}')
        for l in lines:
            strall+=l;
    print(f'strall={strall}')
    # 逐行读取,查看是否有图片的连接
    for i in lines:
        # res = '!\[\[(.*?)\]\]'
        # result = re.search(res, i)
        # print(i,result)
        # if(result!=None):
        #     print(result.group(1))
        #     nameImage,pathImage=getimagePath(filepath,result.group(1))
        #     newPathImage=filepath+'\\life\\assets'
        #     if(os.path.exists(newPathImage)==False):
        #         os.makedirs(newPathImage);
        #     remove_file(pathImage,newPathImage,nameImage);
        print(f'i={i}')
        nameImage,pathImage=checkIsImagelink(filepath,i);
        if(nameImage!=None):
            moveImageToDest(pathImage,new_path_note,nameImage);
