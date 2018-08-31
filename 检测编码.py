import chardet
import urllib
 
#可根据需要，选择不同的数据
TestData = urllib.urlopen('http://www.baidu.com/').read()
print chardet.detect(TestData)
 
运行结果：
{'confidence': 0.99, 'encoding': 'GB2312'}




import urllib
from chardet.universaldetector import UniversalDetector
usock = urllib.urlopen('http://www.baidu.com/')
#创建一个检测对象
detector = UniversalDetector()
for line in usock.readlines():
	#分块进行测试，直到达到阈值
    detector.feed(line)
    if detector.done: break
#关闭检测对象
detector.close()
usock.close()
#输出检测结果
print detector.result
 
运行结果：
{'confidence': 0.99, 'encoding': 'GB2312'}




#直接判断
#!/usr/bin/env python
# coding=utf-8
import chardet

a = "\260\332\266\311\311\350\261\270\310\325\326\276\312\325\274\257\304\243\277\351"
fencoding = chardet.detect(a)  #这行可以判断当前字符串的格式，以便后面设置打印字符的字符编码

print(fencoding)
a = a.decode('gbk')
print(a)