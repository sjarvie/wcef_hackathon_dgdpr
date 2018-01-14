import tornado.ioloop
import tornado.web
import json
from npre import bbs98 #  noqa
import base64
import ipdb

def encode_bytes_to_base_64_str(data):
    encoded = base64.b64encode(data)
    return bytes.decode(encoded)

def decode_base64_str_into_bytes(s):
    encoded = str.encode(s)
    return base64.b64decode(encoded)


class NucypherTestHandler(tornado.web.RequestHandler):
    def get(self):
        out = 'Test doing some crypto!'
        print(out)
        self.write(out)

    def post(self):
        args = json.loads(self.request.body)
        # test an object can be created
        print('Got args {}'.format(args))

        # encrypt some data
        pre = bbs98.PRE()
        p_k = decode_base64_str_into_bytes(args['p_k'])
        # p_k_encoded = str.encode(args['p_k'])
        # p_k = b64decode(p_k_encoded)


        msg = args['msg']
        emsg = pre.encrypt(p_k, msg)


        emsg_encoded = base64.b64encode(emsg)

        # ipdb.set_trace()

        out = {
            'emsg': bytes.decode(emsg_encoded)
        }
        self.write(
            json.dumps(out)
        )



