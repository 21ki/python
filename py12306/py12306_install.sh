wget -O env.py https://raw.githubusercontent.com/pjialin/py12306/master/env.docker.py.example
docker run -d -p 8008:8008 --name=py12306 -v $(pwd):/config -v data:/data pjialin/py12306


#最先安装2019年9月10日 15:58:07
git clone https://github.com/pjialin/py12306
pip install -r requirements.txt
