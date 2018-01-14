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


class SharesHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def initialize(self, keys):
        self.keys = keys

    def get(self):
        """
        USAGE: GET /shares?filename=<filename>&sender=<b64 sender public key>
        """

        filename = self.get_argument("filename")
        sender_b64 = self.get_argument("sender")

        print(
          'getting shares with args \n\t\t fname {} \n\t\t sender {}'.format(filename, sender_b64)
        )
        print('getting shares, keys are {}'.format(self.keys))

        response = dict(shares=[])

        for recipient, data in self.keys.get(sender_b64, {}).get(filename, {}).items():
            response["shares"].append({
                "name": data["name"],
                "key": data["key"]
                })

        # test an object can be created
        self.write(response)


    def post(self):
        """
        Expects POSTed payload
        {
          "sender": "<b64 public key of sender>",
          "reciever": "<b64 public key of receiver>",
          "name": "<name of the receiver>",
          "filename": "<name of file to share>",
          "rekey": "<base 64 encoded rekey>",
          "encryptedEphemeralKey": "<base 64 ephemeral key encrypted with the receiver’s public key>"
        }
        """
        args = json.loads(self.request.body)
        sender_b64 = args['sender']
        receiver_b64 = args['receiver']
        filename = args['filename']
        name = args['name']
        rekey_b64 = args['rekey']


        encryptedEphemeralKey_b64 = args['encryptedEphemeralKey']

        self.keys.setdefault(sender_b64, {}).setdefault(filename, {})[receiver_b64] = {
                "name": name,
                "key": receiver_b64,
                "rekey": rekey_b64,
                "encryptedEphemeralKey": encryptedEphemeralKey_b64
                }
        self.write("OK")

    def delete(self):
        """
        {
          "sender": "<b64 public key of sender>",
          "receiver": "<b64 public key of receiver>",
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

