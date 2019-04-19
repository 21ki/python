# -*- coding:utf-8 -*-
import requests
import tornado.ioloop
import tornado.web

phonenumber = "xxxxxxx,xxxxxxx"
portdic = {
    "9876":"服务类型MQ,端口9876",
    "2181":"服务类型ZK,端口2181",
    "3306":"服务类型数据库,端口3306",
    "27017":"服务类型数据库,端口27017",
    "1908":"服务类型spada,薛亮应用",
    "53":"服务类型dns,端口53",
    "9200":"服务类型es,端口9200",
    "6379":"服务类型redis,端口6379",
    "80":"服务类型nginx,端口80"
}
statusdic = {
    "PROBLEM":"服务发生故障",
    "OK":"故障恢复"
}

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        status = self.get_argument('status')
        endpoint = self.get_argument('endpoint')
        metric = self.get_argument('metric')
        tags = self.get_argument('tags')
        statusok = statusdic.get(status)
        port = tags.split(":")[1]
        p_endpoint = endpoint.split(".")
        del(p_endpoint[0])
        portmes = portdic.get(port)
        if portmes == None:
            portmes = "端口" + port
        # 短信
        requests.get("http://域名/send_sms/%s,%s,%s,%s/%s"%(statusok,endpoint,metric,portmes,phonenumber))
        # 电话
        requests.get("http://域名/send_phone/%s%s%s%s/%s"%(statusok,p_endpoint,metric,portmes,phonenumber))
        message = status + endpoint + metric + tags
        print(status,endpoint,metric,tags,port)
application = tornado.web.Application([(r"/message", MainHandler), ])
if __name__ == "__main__":
    application.listen(8868)
    tornado.ioloop.IOLoop.instance().start()