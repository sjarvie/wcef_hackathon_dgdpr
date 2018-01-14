import requests
import json
from npre import bbs98 #  noqa
import base64
import ipdb

base_url = 'http://localhost:8888'
fname = 'testfile.txt'

r = requests.get(
    '{}/s3_handler/{}'.format(base_url, fname)
)


print('received response \n {}'.format(r.text))

