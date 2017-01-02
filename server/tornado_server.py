# encoding: utf8
import tornado.ioloop
import tornado.web
import tornado.escape
from delay_response import DelayHandler

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")

    def post(self):
        args = self.request.arguments
        print args
        self.write(tornado.escape.json_encode(args))

def make_app():
    return tornado.web.Application([
        (r"/test", TestHandler),
        (r"/delay", DelayHandler),
    ])

def tornadoThread():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    tornadoThread()