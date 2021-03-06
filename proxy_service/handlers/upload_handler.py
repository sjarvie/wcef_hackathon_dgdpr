import json
import base64
import ipdb
import boto
import requests
import tornado.ioloop
import tornado.web

from boto.s3.key import Key

CONN = boto.connect_s3(is_secure=False)
BUCKET = 'wcef-2018-dgdp'

def encode_bytes_to_base_64_str(data):
    encoded = base64.b64encode(data)
    return bytes.decode(encoded)

def decode_base64_str_into_bytes(s):
    encoded = str.encode(s)
    return base64.b64decode(encoded)


class UploadHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

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
        print('uploading file')

        fname = args['filename']
        c_b64 = args['ciphertext']
        edek_b64 = args['edek']
        sender_b64 = args['sender']

        # format is /public_key/fname
        k_base = '/{}/{}'.format(sender_b64, fname)
        bucket = CONN.get_bucket(BUCKET)

        # upload ciphertext
        # import pdb; pdb.set_trace()
        k_ciphertext = '{}/ciphertext'.format(k_base)
        upload_ciphertext = Key(bucket)
        upload_ciphertext.key = k_ciphertext
        upload_ciphertext.set_contents_from_string(c_b64)

        print('uploaded cipher text to {}'.format(k_ciphertext))

        # upload edek
        # import pdb; pdb.set_trace()
        k_edek = '{}/edek'.format(k_base)
        upload_edek = Key(bucket)
        upload_edek.key = k_edek
        upload_edek.set_contents_from_string(edek_b64)
        print('uploaded edek text to {}'.format(k_edek))


        self.write("OK")

