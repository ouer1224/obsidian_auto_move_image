#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import shutil
import os
import re

logname=r'D:\note_base\obsidian\log.txt'
enable_print = False;


def no_output(self, *args, sep=' ', end='\n', file=None):
    return;



if (enable_print == False):
    print = no_output;
    print(f'test err')

def getfilePath():
    # for i in sys.argv:
    print(f"sys.argv={sys.argv}")
    filename = sys.argv[-1];
    filepath = sys.argv[-2]
    filepath=filepath.replace('/', '\\')
    tmpstr=filepath.split('\\')
    filename=tmpstr[-1];
    filepath='\\'.join(tmpstr[0:-1])
    print(f'name={filename}, path={filepath}')
    return filename, filepath

def savePathInfor(filepath):
    with open(logname, 'w+') as fp:
        fp.write(filepath)
    
    return True;



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
    #print(f's={s}')
    print(result)
    nameImage=''
    pathImage=''
    if(result==None):
        return None,None;
    else:
        print(result);
        tmp=result.group(1);
        #print(f"tmp={tmp}")
        tmp=tmp.split('/')
        pathImage=root+'\\'+tmp[0]
        nameImage=tmp[1]
        return nameImage,pathImage

def moveImageToDest(imagePath, new_note_path, filename):
    tmp=imagePath.split('\\')
    tmp=tmp[-1]
    new_path=new_note_path+'\\'+tmp;
    if(os.path.exists(new_path)!=True):
        os.makedirs(new_path)
    imagefile=imagePath+'\\'+filename;

    if(os.path.isfile(imagefile)==True):
        remove_file(imagePath, new_path, filename);
    else:
        print(f'err----no imagefile = {imagefile}')
    

def readPathInfor():
    fname=''
    fpath=''
    
    with open(logname, 'r') as fp:
        allline=fp.readlines()
        if(len(allline)>2):
            return None;
        fname=allline[1];
        fpath=allline[0];
        return fname, fpath;



if __name__ == '__main__':

    # 记录当前文件的路径到log.txt中, 第一行是source, 第二行是dest.
    oldfilename, oldfilepath=readPathInfor()
    oldfilepath=oldfilepath.replace('\n', '')
    print(f'oldfname={oldfilename}, oldfpath={oldfilepath}')
    newfilename, newfilepath=getfilePath()
    print(f'newfname={newfilename}, newfpath={newfilepath}')
    
    if(oldfilename!=newfilename):
        print(f"err:--no same file")
    else:
            
        with open(newfilepath+'\\'+newfilename, 'r', encoding='utf-8') as fp:
            alllines=fp.readlines()
            for i in alllines:
                nameimage, pathimage=checkIsImagelink(oldfilepath, i);
                if(nameimage!=None):
                    print(f'nameI={nameimage}, pathI={pathimage}')
                    moveImageToDest(pathimage,newfilepath, nameimage);
        


            
        

