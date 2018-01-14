import tornado.ioloop
import tornado.web
import boto
import json
from npre import bbs98 #  noqa
import base64
import ipdb

CONN = boto.connect_s3(is_secure=False)
BUCKET = 'wcef-2018-dgdp'



def encode_bytes_to_base_64_str(data):
    encoded = base64.b64encode(data)
    return bytes.decode(encoded)

def decode_base64_str_into_bytes(s):
    encoded = str.encode(s)
    return base64.b64decode(encoded)


class DownloadHandler(tornado.web.RequestHandler):

    def initialize(self, keys):
        self.keys = keys


    def post(self):
        args = json.loads(self.request.body)
        # test an object can be created
        print('Download function got args {}'.format(args))

        # encrypt some data
        pre = bbs98.PRE()

        fname = args['filename']
        sender_b64 = args['sender']
        receiver_b64 = args['receiver']

        sender = decode_base64_str_into_bytes(sender_b64)
        receiver = decode_base64_str_into_bytes(receiver_b64)

        # first, fetch the ciphertext and edek from S3
        # format is /public_key/fname
        k_base = '/{}/{}'.format(sender_b64, fname)
        bucket = CONN.get_bucket(BUCKET)

        # download ciphertext
        k_ciphertext = '{}/ciphertext'.format(k_base)
        c_b64 = bytes.decode(bucket.get_key(k_ciphertext, validate=False).get_contents_as_string())
        print('Got ciphertext from path {}'.format(k_ciphertext))

        # download edek
        k_edek = '{}/edek'.format(k_base)
        edek_b64 = bucket.get_key(k_edek, validate=False).get_contents_as_string()
        print('Got edek from path {}'.format(k_edek))
        edek = decode_base64_str_into_bytes(bytes.decode(edek_b64))

        # next, fetch re_key
        receiver_metadata = self.keys[sender_b64][fname][receiver_b64]
        print(receiver_metadata)
        rekey = decode_base64_str_into_bytes(receiver_metadata['rekey'])

        e_b_b64 = receiver_metadata['encryptedEphemeralKey']

        # now, reencrypt the edek with the re_key
        edek_b = pre.reencrypt(rekey, edek)
        edek_b_b64 = encode_bytes_to_base_64_str(edek_b)


        out = {
            'e_b': e_b_b64,
            'edek_b': edek_b_b64,
            'ciphertext': c_b64
        }


        # ipdb.set_trace()
        self.write(
            json.dumps(out)
        )



