import json
import base64

import ipdb
import boto
import requests
import tornado.ioloop
import tornado.web

from boto.s3.key import Key


CONN = boto.connect_s3()
BUCKET = 'wcef-2018-dgdp'


def encode_bytes_to_base_64_str(data):
    encoded = base64.b64encode(data)
    return bytes.decode(encoded)

def decode_base64_str_into_bytes(s):
    encoded = str.encode(s)
    return base64.b64decode(encoded)



class UploadHandler(tornado.web.RequestHandler):

    def post(self):
        """
        {
            “filename”: “<filename>”,
            “ciphertext”: “<base64-encoded binary ciphertext>”,
            “edek”: “<base64-encoded encrypted symmetric key> ”
            “sender”: “<base64-encoded sender's public key>
        }

        """
        args = json.loads(self.request.body)


        # test an object can be created
        print('Got args {}'.format(args))

        fname = args['filename']
        c_b64 = args['ciphertext']
        edek_b64 = args['edek']
        sender_b64 = args['sender']

        # format is /public_key/fname
        k_base = '/{}/{}'.format(sender_b64, fname)
        bucket = CONN.get_bucket(BUCKET)

        # upload ciphertext
        import pdb; pdb.set_trace()
        k_ciphertext = '{}/ciphertext'.format(k_base)
        upload_ciphertext = Key(bucket)
        upload_ciphertext.key = k_ciphertext
        upload_key.set_contents_from_string(c_b64)


        # upload edek
        import pdb; pdb.set_trace()
        k_edek = '{}/ciphertext'.format(k_base)
        upload_edek = Key(bucket)
        upload_edek.key = k_ciphertext
        upload_key.set_contents_from_string(edek_b64)



        self.write("OK")




