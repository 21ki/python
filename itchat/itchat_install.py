yum install epel-release
yum install python34
curl -O https://bootstrap.pypa.io/get-pip.py
/usr/bin/python3.4 get-pip.py
python3
yum install python-pip
pip3 install itchat
python3 -c "import itchat"


#微信扫描登陆
#hotReload=True 登陆保持  enableCmdQR=2 linux和unix 终端输出二维码
vi login.py
import itchat


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])

itchat.auto_login(hotReload=True,enableCmdQR=2)
itchat.run()