import tornado.ioloop
import tornado.web

from handlers.shares_handler import SharesHandler
from handlers.files_handler import FilesHandler
from handlers.upload_handler import UploadHandler
from handlers.download_handler import DownloadHandler


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
        (r"/upload", UploadHandler),
        (r"/files", FilesHandler),
        (r"/shares", SharesHandler, dict(keys=keys)),
        (r"/upload", UploadHandler),
        (r"/download", DownloadHandler, dict(keys=keys))
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
