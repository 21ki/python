#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
MESSAGE = '文件已经存在'
TESTDIR = 'testdir' #创建的文件夹名称
try:
    home = os.path.expanduser("~")
    print(home)
    if not os.path.exists(os.path.join(home, TESTDIR)):
        os.makedirs(os.path.join(home, TESTDIR))
    else:
        print(MESSAGE)
except Exception as e:
    print(e)