import subprocess
import os
'''
https://zhuanlan.zhihu.com/p/100946961
'''

def subprocess_():
    """
    subprocess模块执行linux命令
    :return:
    """
    subprocess.call("ls") # 执行ls命令


def system_():
    """
    system模块执行linux命令
    :return:
    """
    # 使用system模块执行linux命令时，如果执行的命令没有返回值res的值是256
    # 如果执行的命令有返回值且成功执行，返回值是0
    res = os.system("ls")


def popen_():
    """
    popen模块执行linux命令。返回值是类文件对象，获取结果要采用read()或者readlines()
    :return:
    """
    val = os.popen('ls').read() # 执行结果包含在val中


def main():
    subprocess_() # 方法1
    system_() # 方法2
    popen_() # 方法3


if __name__ == '__main__':
    main()