#在deploy节点安装及准备ansible
# Ubuntu 16.04 
apt-get install git python-pip -y
# CentOS 7
yum install git python-pip -y
# pip安装ansible(国内如果安装太慢可以直接用pip阿里云加速)
#pip install pip --upgrade
#pip install ansible
pip install pip --upgrade -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
pip install --no-cache-dir ansible -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

在Ubuntu 16.04中，如果出现以下错误:

Traceback (most recent call last):
  File "/usr/bin/pip", line 9, in <module>
    from pip import main
ImportError: cannot import name main
将/usr/bin/pip做以下修改：

#原代码
from pip import main
if __name__ == '__main__':
    sys.exit(main())

#修改后
from pip import __main__
if __name__ == '__main__':
    sys.exit(__main__._main())

在deploy节点配置免密码登陆
ssh-keygen -t rsa -b 2048 回车 回车 回车
ssh-copy-id $IPs #$IPs为所有节点地址包括自身，按照提示输入yes 和root密码


mkdir -p /etc/ansible