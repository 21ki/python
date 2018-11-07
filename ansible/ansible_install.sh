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



#ansible 启动tomcat报错
fatal: [192.168.1.104]: FAILED! => {"changed": true, "cmd": "sh /opt/tomcat-test-8081/bin/startup.sh", "delta": "0:00:00.026094", "end": "2018-11-07 14:18:49.051533", "msg": "non-zero return code", "rc": 1, "start": "2018-11-07 14:18:49.025439", "stderr": "", "stderr_lines": [], "stdout": "Neither the JAVA_HOME nor the JRE_HOME environment variable is defined\nAt least one of these environment variable is needed to run this program", "stdout_lines": ["Neither the JAVA_HOME nor the JRE_HOME environment variable is defined", "At least one of these environment variable is needed to run this program"]}
        to retry, use: --limit @/root/ansible/tomcat-deploy-192.168.1.104.retry
#查找问题
ansible tomcat-104-8181 -m shell -a "java -version"
发现不能远程调用java环境

原因是ansible 调用java没有找到环境变量（/bin目录下没有找到Java命令所以报错）
#参考连接https://blog.csdn.net/u014505701/article/details/70062697
#执行一下命令 问题解决
ln -s /usr/local/jdk1.8.0_181/bin/jar /bin/jar
ln -s /usr/local/jdk1.8.0_181/bin/java /bin/java
ln -s /usr/local/jdk1.8.0_181/bin/javac /bin/javac
ln -s /usr/local/jdk1.8.0_181/bin/javah /bin/javah
ln -s /usr/local/jdk1.8.0_181/bin/javadoc /bin/javadoc
