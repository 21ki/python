import requests
import re
from time import sleep
from multiprocessing import Pool, Manager
#from requests_html import HTMLSession
def test_ip(ip,port):
    #print (ip)
    try:
        #requests.get('http://www.baidu.com/', proxies={"http":"http://"+ip+':'+port},timeout=2)
        #session = Session()
        proxy = {
            "http": "socks5://"+ip+':'+port,
            "https": "socks5://"+ip+':'+port
            }
        url = "http://www.youtube.com/"
        req = requests.get(url, proxies=proxy)
        print (req)
    except:
        print ('connect failed')
        a=1
    else:
        print (ip+':'+port)
        save=open('p.txt','a+')
        save.write(ip+':'+port+"\n")
        save.close()
        #print 'success'
def test():
      path = 'ip.txt'
      p = Pool(200)
      q = Manager().Queue()
      fr = open(path, 'r')
      rtar = fr.readlines()
      fr.close()
      for i in range(len(rtar)):
          ruleip=re.compile('(.*?):')
          try:
            rip =(ruleip.findall(rtar[i]))[0]
          except:
            rip = str(rtar[i]).strip('\n')
          ruleport=re.compile(':(.*)')
          try:
            rport=ruleport.findall(rtar[i])[0]
          except:
            rport='80'
        #time.sleep(1)
          #tmain(rip,rport)
          p.apply_async(test_ip,args=(rip,rport))
      p.close()
      p.join()
if __name__ == '__main__':
    #serverInput = raw_input('IP Router: ')
    #test_ip('192.168.43.208','1088')
    #test_ip('192.168.66.54','1080')
    test()
