
import re



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