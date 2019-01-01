# -*- coding: utf-8 -*-
__author__ = 'dongnanzhy'

import os
import tornado.ioloop
import tornado.web


# Tornado web 主要模块
#    1. tornado.web Application 和 RequestHandler类处理http
#    2. tornado.template 模板渲染
#    3. tornado.routing 路由


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("base.html", msg="hello hello hello")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        debug=True
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()