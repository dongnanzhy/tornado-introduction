# -*- coding: utf-8 -*-
__author__ = 'dongnanzhy'

import tornado.ioloop
import tornado.web
import tornado.gen
import tornado.httpclient
import requests

import time

N = 3
URL = 'http://localhost:8888/sleep'


@tornado.gen.coroutine
def main():
    http_client = tornado.httpclient.AsyncHTTPClient()
    responses = yield [
        http_client.fetch(URL) for i in range(N)
    ]

beg1 = time.time()
tornado.ioloop.IOLoop.current().run_sync(main)
print("async", time.time()-beg1)

beg2 = time.time()
for i in range(N):
    requests.get(URL)
print("sync req", time.time()-beg2)