#下载安装包
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
#创建文件夹
mkdir /usr/local/python3 
tar -xvJf  Python-3.7.0.tar.xz
cd Python-3.7.0
./configure --prefix=/usr/local/python3
make && make install

ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3




#yum安装python3
yum install -y python36
cd /usr/bin
ln -s python3.6 python3

#yum pip
yum install python36-setuptools
easy_install-3.6 pip



#参照k8s安装
#每个节点运行
# 文档中脚本默认均以root用户执行
# 安装 epel 源并更新
yum install epel-release -y
yum update
# 安装python
yum install python -y


#在deploy节点安装及准备ansible
# CentOS 7
yum install git python-pip -y
# pip安装ansible(国内如果安装太慢可以直接用pip阿里云加速)
#pip install pip --upgrade
#pip install ansible
pip install pip --upgrade -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
pip install --no-cache-dir ansible -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com



#python 3.7 源码安装
#安装依赖
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel
yum install python-pip
pip install wget
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
tar -zxvf Python-3.7.0.tgz
./configure prefix=/usr/local/python3 
make && make install
ln -s /usr/local/python3/bin/python3.7 /usr/bin/python
ln -s /usr/local/python3/bin/pip3.7 /usr/bin/pip
python -V
pip -V

#解决yum无法安装问题
vi /usr/bin/yum 
把 #! /usr/bin/python 修改为 #! /usr/bin/python2 
vi /usr/libexec/urlgrabber-ext-down 
把 #! /usr/bin/python 修改为 #! /usr/bin/python2


#报错ImportError: libSM.so.6: cannot open shared object file: No such file or directory
yum install libSM-1.2.2-2.el7.x86_64 --setopt=protected_multilib=false
#ImportError: libXext.so.6: cannot open shared object file: No such file or directory
yum whatprovides libXext.so.6
yum install -y libXext-1.3.3-3.el7.i686
yum install libXext.x86_64



yum install -y wget ntpdate glibc.i686
yum install libstdc++

strings /usr/lib64/libstdc++.so.6.0.19 | grep CXXABI_

#gcc安装 link https://www.jianshu.com/p/f7cd0e2416b9
https://medium.com/@t1neo/2-ways-of-usr-lib64-libstdc-so-5-version-cxxabi-1-3-8-glibcxx-3-4-20-not-found-decd76c10db1