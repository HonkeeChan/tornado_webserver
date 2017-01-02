# encoding: utf8
import tornado.ioloop
import tornado.web
import tornado.escape
import time


class DelayHandler(tornado.web.RequestHandler):
    def get(self):
    	time.sleep(30)
        self.write("hello world")

    def post(self):
        delayTime = self.get_argument("time", default=30)
        time.sleep(delayTime)
        self.write("delay " + str(delayTime))