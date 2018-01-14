import tornado.ioloop
import tornado.web

from handlers.nucypher_test_handler import NucypherTestHandler


class HelloWorldHandler(tornado.web.RequestHandler):
    def get(self):
        out = 'Hello World!'
        print(out)
        self.write(out)

def make_app():
    return tornado.web.Application([
        (r"/hello_world", HelloWorldHandler),
        (r"/nucypher_test_handler", NucypherTestHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
