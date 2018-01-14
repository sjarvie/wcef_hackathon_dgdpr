import tornado.ioloop
import tornado.web
import json

import pyaes
from npre import bbs98 #  noqa
import base64
import ipdb

def encode_bytes_to_base_64_str(data):
    encoded = base64.b64encode(data)
    return bytes.decode(encoded)

def decode_base64_str_into_bytes(s):
    encoded = str.encode(s)
    return base64.b64decode(encoded)

pre = bbs98.PRE()



class GenPrivHandler(tornado.web.RequestHandler):
    """ Generate a private key encoded as base 64 str"""
    def get(self):
        data = pre.gen_priv(dtype=bytes)

        out = encode_bytes_to_base_64_str(data)
        print('gen private key {}'.format(out))
        self.write(out)

class RekeyHandler(tornado.web.RequestHandler):
    """ Generates a rekey from sk_in to sk_out
    Generate a private key encoded as base 64 str
    :args
       sk_in : base64 encoded str
       sk_out : base64 encoded str
    :return re_ab: base64 encoded str

    """
    def post(self):
        args = json.loads(self.request.body)
        sk_in = decode_base64_str_into_bytes(args['sk_in'])
        sk_out = decode_base64_str_into_bytes(args['sk_out'])
        re_ab = pre.rekey(sk_in, sk_out)
        out = encode_bytes_to_base_64_str(re_ab)
        print('gen rekey {}'.format(out))
        self.write(out)


class EncryptHandler(tornado.web.RequestHandler):
    """ Encrypts data using public key

    :args
       pk : base64 encoded str
       data : base64 encoded str
    :return e_b: encrypted data as base64 str

    """
    def post(self):
        args = json.loads(self.request.body)
        pk = decode_base64_str_into_bytes(args['pk'])
        data = decode_base64_str_into_bytes(args['data'])
        e_b = pre.encrypt(pk, data)
        out = encode_bytes_to_base_64_str(e_b)
        print('gen ecrypt {}'.format(out))
        self.write(out)




class DecryptHandler(tornado.web.RequestHandler):
    """ Decrypts data using secret key

    :args
       sk : base64 encoded str
       c : base64 encoded str
    :return data: decrypted data as base64 str?

    """
    def post(self):
        args = json.loads(self.request.body)
        sk = decode_base64_str_into_bytes(args['sk'])
        c = decode_base64_str_into_bytes(args['c'])
        data = pre.decrypt(sk, c)
        out = encode_bytes_to_base_64_str(data)

        print('gen decrypt {}'.format(out))
        self.write(out)



class EncryptAESHandler(tornado.web.RequestHandler):
    """ Encrypts data using AES symmetric key

    :args
       dek : str symmetric key
       data : base64 encoded str
    :return c: encrypted data as base64 str

    """
    def post(self):
        iv = "InitializationVe"

        args = json.loads(self.request.body)
        dek = str.encode(args['dek'])
        data = decode_base64_str_into_bytes(args['data'])
        c = pyaes.AESModeOfOperationCTR(dek).encrypt(data)
        out = encode_bytes_to_base_64_str(c)
        print('gen encrypt aes {}'.format(out))
        self.write(out)


class DecryptAESHandler(tornado.web.RequestHandler):
    """ Encrypts data using public key

    :args
       dek : str symmetric key
       c : base64 encoded str
    :return data: decrypted data as base64 str

    """
    def post(self):
        iv = "InitializationVe"
        args = json.loads(self.request.body)
        dek = str.encode(args['dek'])
        c = decode_base64_str_into_bytes(args['c'])
        data = pyaes.AESModeOfOperationCTR(dek).decrypt(c)
        out = encode_bytes_to_base_64_str(data)
        print('gen decrypt aes {}'.format(out))
        self.write(out)




def make_app():
    return tornado.web.Application([
        (r"/gen_priv", GenPrivHandler),
        (r"/rekey", RekeyHandler),
        (r"/encrypt", EncryptHandler),
        (r"/decrypt", DecryptHandler),
        (r"/encrypt_aes", EncryptAESHandler),
        (r"/decrypt_aes", DecryptAESHandler),

    ])



if __name__ == "__main__":
    app = make_app()
    app.listen(8889)
    tornado.ioloop.IOLoop.current().start()
