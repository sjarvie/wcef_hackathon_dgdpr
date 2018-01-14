import json
import base64

import ipdb
import boto
import requests
import tornado.ioloop
import tornado.web



CONN = boto.connect_s3()
BUCKET = 'wcef-2018-dgdp'



class S3Handler(tornado.web.RequestHandler):

    def get(self, fname):
        """
        Get file fname from bucket as string
        """
        bucket = CONN.get_bucket(BUCKET, validate=False)
        ipdb.set_trace()
        # keys = bucket.get_all_keys()
        k = bucket.get_key(fname, validate=False)
        print('Getting contents')
        out = k.get_contents_as_string() # print as string
        self.write(out)

