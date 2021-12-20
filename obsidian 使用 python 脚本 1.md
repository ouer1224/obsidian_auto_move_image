> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/391846157)

一、说明
----

obsidian 是一个由 ES6 开发的软件，它本身支持开发插件来实现我们自己想要的功能。但是另一种语言壁垒却使我们望而却步。现在就有一种方式，可以让 obsidian 调用 cmd 命令，而 cmd 命令又可以调用如：python、C 语言、cmd 命令等各种程序，大大方便了我们的开发。

二、实现方式
------

1、首先下载 Templater 插件
-------------------

*   Github 下载 [https://github.com/SilentVoid13/Templater/archive/refs/heads/master.zip](https://link.zhihu.com/?target=https%3A//github.com/SilentVoid13/Templater/archive/refs/heads/master.zip)

2、配置 Templater
--------------

![](assets/v2-bed6554877be3b4dc8bdbf4370fcea02_r.jpg)

1、设置插件使用的模板的路径（需要自己设置的模板位置，建议和原有的模板分开）

2、设置插件使用的插件的路径（需要自己设置的插件位置）

3、设置 cmd 文件的路径。一般是 **`C:\Windows\System32\cmd.exe`**

4、简单建立一个 Python 脚本，用于测试功能。

*   getname  
    这个名字可以自己指定  
    
*   python ./G4 归档资料 //1 学习 // 模板 //templater// 插件 //getinput.py <% tp.file.path() %> <% tp.file.path(true) %>  
    python 文件的路径是相对于库的路径的，需要修改为自己的文件相对于库顶层目录的相对路径。后面的原样复制（这个内容下面解释）。  
    

3、程序
----

*   **getinput.py** 这个程序只是打印传入的参数，并将它们打印出来。这个插件会将打印出来的内容，放到我们正在编辑的位置。return 返回的内容是没有用的。

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def test():
    for i in sys.argv:
        print(i)
    print('测试\n')   
    return "hello"

if __name__ == '__main__':
    test()

```

*   模板：**python 测试. md** 这个文件内，放入下面的内容就可以。getname 和前面配置里的名字相同，前面是什么，这里就是什么。

```
<% tp.user.getname() %>

```

4、效果
----

打印出来 3 行，

第一行是 python 文件的相对路径

第二行是`<% tp.file.path() %>`，这是现在编辑文件的绝对路径

第三行是`<% tp.file.path(true) %>`，这个是现在编辑文件相对于库的相对路径。

通过这两个字符串的相减，我们也就得到库的绝对路径了。**这样我们就可以进行 python 脚本的开发了。**

![](assets/v2-810a43995bf8862de24ceb427d758e8c_r.jpg.png)

问题
--

字符乱码问题
------

现象：

![](assets/v2-3c317b32f4bae625e7c2b4362d2ff125_r.jpg)

解决方案：

1. 按键盘 **Win+R**

2. 输入 **intl.cpl**

3. 选择管理

![](assets/v2-95f3fb710e61955b7172ec9a0408311f_r.jpg)

4. 点击 **更改系统区域设置**

![](assets/v2-4c8ff630aaa59a381612e0d3fbeefd98_r.jpg)

5. 将这个进行勾选

![](assets/v2-755a7fa2d92292b1b608aeecbefe9249_r.jpg)

6. 点击确定之后，需要重启系统。重启完后，就解决问题了。

环境
--

**系统版本**：Window10 x64 1909

**软件版本**：obsidian v0.12.10

**插件版本**：Templater 1.8.1