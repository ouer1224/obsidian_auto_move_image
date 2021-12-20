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
    strpath = filepath.split('/')
    filepath = strpath[0]
    print(f'name={filename}, path={filepath}')
    return filename, filepath


def remove_file(old_path, new_path, filename):
    print(old_path)
    print(new_path)

    src = os.path.join(old_path, filename)
    dst = os.path.join(new_path, filename)
    print('src:', src)
    print('dst:', dst)
    shutil.move(src, dst)



if __name__ == '__main__':
    print('start move')
    filename, filepath=getfilePath()
    print(f'filename={filename}, patj={filepath}')
    newpath=filepath+'\\life'
    print(f'filepath={filepath}, newpath={newpath}')
    remove_file(filepath, newpath, filename)
    print(f' move end')