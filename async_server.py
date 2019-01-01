# -*- coding: utf-8 -*-
__author__ = 'dongnanzhy'

# HTTP 服务器和客户端 (async_server.py + async_client.py)
#   异步操作: @gen.coroutine

# 异步网络模块
# 异步 networking
#   1. tornado.ioloop 事件循环
#   2. tornado.iostream 非阻塞socket封装
#   3. tornado.tcpserver 和tornado.tcpclient

# 协程和并发模块
# 协程和并发
#   1. tornado.gen 协程模块
#   2. tornado.locks/tornado.queues 同步，协程队列模块

import tornado.ioloop
import tornado.web
import tornado.gen
import tornado.httpserver

from datetime import datetime
import time


class SleepHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args):
        yield tornado.gen.sleep(5)
        self.write(str(datetime.now()))


if __name__ == "__main__":
    app = tornado.web.Application(
        [(r'/sleep', SleepHandler)],
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    print("server start on 8888")
    tornado.ioloop.IOLoop.current().start()