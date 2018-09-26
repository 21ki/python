#pip安装

#安装方式1
wget  http://python-distribute.org/distribute_setup.py  
sudo python distribute_setup.py  
wget  https://github.com/pypa/pip/raw/master/contrib/get-pip.py  
sudo python get-pip.py  


#安装方式2
wget https://pypi.python.org/packages/source/p/pip/pip-1.3.1.tar.gz --no-check-certificate   
tar xvf pip-1.3.1.tar.gz  
python pip-1.3.1/setup.py install  


#安装方式3
wget https://bootstrap.pypa.io/get-pip.py  
python get-pip.py  
pip -V　　#查看pip版本

