import tornado.ioloop
import tornado.web

# from handlers.nucypher_test_handler import NucypherTestHandler
from handlers.upload_handler import UploadHandler
from handlers.shares_handler import SharesHandler

keys = {
    "sender": {
        "filename": {
            "receiver": {
                "name": "Donald Trump",
                "key": "test key",
                "rekey": "test rekey",
                "encryptedEphemeralKey": "test ephemeral key"
                }
            }
        }
    }

def make_app():
    return tornado.web.Application([
        # (r"/nucypher_test_handler", NucypherTestHandler),
        # (r"/s3_handler/([a-z_.]*)", S3Handler),
        (r"/upload/", UploadHandler),
        (r"/shares/", SharesHandler, dict(keys=keys))
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
