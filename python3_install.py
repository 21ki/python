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