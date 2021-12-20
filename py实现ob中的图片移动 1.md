
## 实现方式
目前使用py暂时实现了对md文件中图片的移动问题.参考的是[[obsidian 使用 python 脚本]]中对`Templater`插件的使用方式.


## 使用方法
使用方式如下:
1. 打开需要移动的文件,按下快捷键`alt + E`,选择![[assets/Pasted image 20211220133204.png]] 中的`py run getfilepath`.
2. 在ob中自带的文件管理树中,移动笔记.
3. 移动完毕后,按下`alt+E`.在调出的界面中选择`py run moveimage`.此时就完成了对图片的移动.

## 注意事项:
1. 移动前笔记的图片链接必须是**相对本笔记的相对路径**,如果不是,会出现错误.
2. 笔记中有多个对同一个图片的相同链接,在移动以后后,就无法再old目录中找到此图片了,会出现报错,但是不影响移动结果.
3. 移动前的笔记信息存储在了**笔记库的最外层的log.txt**中.

## 缺陷:
1. 必须操作两次才行,比较麻烦
2. 每次执行操作后,都会在鼠标的当前位置插入2个空行,**暂时不清楚这两个空行的来源**.


getfilepath代码如下:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import shutil
import os

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
    filename, filepath=getfilePath()
    print(f'main---filename={filename}, path={filepath}')
    savePathInfor(filepath+'\n'+filename)

```


moveimage代码如下:
```py
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

```