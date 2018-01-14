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


class SharesHandler(tornado.web.RequestHandler):

    def initialize(self, keys):
        self.keys = keys

    def get(self):
        """
        USAGE: GET /shares?filename=<filename>&sender=<sender public key>
        """

        filename = self.get_argument("filename")
        sender = self.get_argument("sender")
        
        response = dict(shares=[])
        for recipient, data in self.keys.get(sender, {}).get(filename, {}).items():
            response["shares"].append({
                "name": data["name"],
                "key": data["key"]
                })

        # test an object can be created
        self.write(json.dumps(response))

    def post(self):
        """
        Expects POSTed payload
        {
          "sender": "<public key of sender>",
          "reciever": "<public key of receiver>",
          "name": "<name of the receiver>",
          "filename": "<name of file to share>",
          "rekey": "<base 64 encoded rekey>",
          "encryptedEphemeralKey": "<base 64 ephemeral key encrypted with the receiver’s public key>"
        }
        """
        args = json.loads(self.request.body)
        sender = args['sender']
        receiver = args['sender']
        filename = args['filename']
        name = args['name']
        rekey = args['rekey']
        encryptedEphemeralKey = args['encyrptedEphemeralKey']
        
        self.keys.setdefault(sender, {}).setdefault(filename, {})[receiver] = {
                "name": name,
                "key": receiver,
                "rekey": rekey,
                "encryptedEphemeralKey": encryptedEphemeralKey
                }
        self.write("OK")

    def delete(self):
        """
        {
          "sender": "<public key of sender>",
          "receiver": "<public key of receiver>",
          "filename": "<filename to revoke access to>"
        }
        """
        args = json.loads(self.request.body)
        sender = args['sender']
        receiver = args['sender']
        filename = args['filename']
        keys = self.keys
        if sender in keys:
            if filename in keys[sender]:
                keys[sender][filename].pop(receiver, None)
                if len(keys[sender][filename]) == 0:
                    keys[sender].pop(filename, None)
                    if len(keys[sender]) == 0:
                        keys.pop(sender, None)
        self.write("OK")
