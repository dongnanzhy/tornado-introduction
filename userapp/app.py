# -*- coding: utf-8 -*-
__author__ = 'dongnanzhy'

# RESTful 风格
#  Resources(资源)：使用URL指向一个实体
#  Representation(表现层)： 资源的表现形式，图片，html等
#  State Transfer(状态转化): GET, POST...等动词操作资源

import tornado.httpserver
import tornado.ioloop
import tornado.web
from handlers import user as user_handlers

HANDLERS = [
    (r"/api/users", user_handlers.UserListHandler),
    (r"/api/users/(\d+)", user_handlers.UserHandler)
]


def run():
    app = tornado.web.Application(
        HANDLERS,
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    port = 8888
    http_server.listen(port)
    print('server start on port: {}'.format(port))
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    run()