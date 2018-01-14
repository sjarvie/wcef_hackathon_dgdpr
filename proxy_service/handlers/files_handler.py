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

# def encode_bytes_to_base_64_str(data):
#     encoded = base64.b64encode(data)
#     return bytes.decode(encoded)
# 
# def decode_base64_str_into_bytes(s):
#     encoded = str.encode(s)
#     return base64.b64decode(encoded)


class FilesHandler(tornado.web.RequestHandler):

    def get(self):
        """
        USAGE: GET /files?sender=<sender public key>
        Returns: 

        {
          "files": [
            "file/name/a.txt",
            ...
          ]
        }
        """
        sender = self.get_argument("sender")

        response = {
                "files": []
                }

        bucket = CONN.get_bucket(BUCKET)
        bucket_keys = bucket.list(sender + "/", delimiter="/")
        transformed_keys = set()
        for key in bucket_keys:
            prefix_striped = key.name[(len(sender) + 1):]
            prefix_postfix_striped = prefix_striped[:prefix_striped.rfind("/")]
            transformed_keys.add(prefix_postfix_striped)
        response = {
                "files": list(transformed_keys)
                }
        self.write(json.dumps(response))
