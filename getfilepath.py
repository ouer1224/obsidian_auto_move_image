#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import shutil
import os


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
    logname=r'D:\note_base\obsidian\log.txt'
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


if __name__ == '__main__':
    # 记录当前文件的路径到log.txt中, 第一行是source, 第二行是dest.
    filename, filepath=getfilePath()
    print(f'main---filename={filename}, path={filepath}')
    savePathInfor(filepath)
