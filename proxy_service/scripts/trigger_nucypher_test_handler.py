import requests
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




s_k = b'\x00\n\x8b\xeb\xc31\x81\x06\xbb\xb8\x92\xa5\x9dO7\xc7\xd1\xcc\x98\xbdM5\xbd\x13\xd9\xb9\x84\xea\xd6\x8e\x89H\xe0'

p_k = b'\x01\x02b\xaa<\xf9\xa2\xe0\xfb\x7f\xaf`\xaa\xc0\xf6l\x8a]h\xfb\xe3\x06\xc9\xd3\xf0\xbf~\\\xe7w+\xea\xf6%'

base_url = 'http://localhost:8888'

p_k_encoded = encode_bytes_to_base_64_str(p_k)

# p_k_encoded = base64.b64encode(p_k)
# p_k_encoded = base64.encodestring(p_k)
payload = {
    'p_k': p_k_encoded,
    'msg': 'Some message to encrypt'
}

r = requests.post(
    '{}/nucypher_test_handler'.format(base_url),
    data=json.dumps(payload)
)


print('received response {}'.format(r.text))

data = json.loads(r.text)

# ipdb.set_trace()

emsg = decode_base64_str_into_bytes(data['emsg'])
# emsg_encoded = str.encode(data['emsg'])
# emsg = base64.b64decode(emsg_encoded)


pre = bbs98.PRE()
msg2 = pre.decrypt(s_k, emsg)

print('Decrypting using secret key gives\n {}'.format(msg2))

import base64
