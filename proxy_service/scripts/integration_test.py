import pyaes
import requests
import uuid
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

pre = bbs98.PRE()



"""


INTEGRATION TEST

TODO: use a file on disk and test with KeyGen server
"""


# Declare Alice's keys
sk_a = b'\x00\n\x8b\xeb\xc31\x81\x06\xbb\xb8\x92\xa5\x9dO7\xc7\xd1\xcc\x98\xbdM5\xbd\x13\xd9\xb9\x84\xea\xd6\x8e\x89H\xe0'
sk_a_b64 = encode_bytes_to_base_64_str(sk_a)

pk_a = b'\x01\x02b\xaa<\xf9\xa2\xe0\xfb\x7f\xaf`\xaa\xc0\xf6l\x8a]h\xfb\xe3\x06\xc9\xd3\xf0\xbf~\\\xe7w+\xea\xf6%'
pk_a_b64 = encode_bytes_to_base_64_str(pk_a)


# the symmetric key
dek = b'd144044f-ba46-41cd-b52e-0e3f046e'


# Declare Bob's keys
sk_b = b"\x00\x030'\xac\xf1 \x913\x0f\xc2\xbf\xfb*\xb53\x8b\xf0\xb6\r[`\x1bM\xc8\xb6\xd5$\x9d2k\xb4\xc7"
sk_b_b64 = encode_bytes_to_base_64_str(sk_b)

pk_b = b'\x01\x02k\x1c{d\xc8Q!\xf9-&\xde\x93\xf7\xf6HqgM\xb8\xf9o\xd1_q4R\xcb-\xb3j\x93\xc0'
pk_b_b64 = encode_bytes_to_base_64_str(pk_b)

base_url = 'http://localhost:8888'

filename = 'integration_test_file.txt'
data = b'Some data that we are hiding in a file on S3'
data_b64 = encode_bytes_to_base_64_str(data)

# encrypt data with dek
iv = "InitializationVe"
c = pyaes.AESModeOfOperationCTR(dek).encrypt(data)
c_b64 = encode_bytes_to_base_64_str(c)


# encrypt dek with alice's pk
edek = pre.encrypt(pk_a, dek)
edek_b64 = encode_bytes_to_base_64_str(edek)
# ipdb.set_trace()


# UPLOAD 
# Alice uploads a file
payload = {
    'filename': filename,
    'ciphertext': c_b64,
    'edek': edek_b64,
    'sender': pk_a_b64
}

resp = requests.post(
    '{}/upload'.format(base_url),
    data=json.dumps(payload)
)


# SHARES

# Alice gets her shares
resp = requests.get(
    '{}/shares'.format(base_url),
    params = {
        'filename': filename,
        'sender': pk_a_b64
    }
)

# shares should be empty
print(resp.text)
print(resp.text == '{"shares": []}')


# Alice sets a shares for bob
emphermeral_key = pre.gen_priv(dtype=bytes)
# rekey
re_ab = pre.rekey(sk_a, emphermeral_key)
re_ab_b64 = encode_bytes_to_base_64_str(re_ab)
# encrypt for Bob
e_b = pre.encrypt(pk_b, emphermeral_key)
e_b_b64 = encode_bytes_to_base_64_str(e_b)

payload = {
    'filename': filename,
    'sender': pk_a_b64,
    'receiver': pk_b_b64,
    'name': 'Bob',
    'rekey': re_ab_b64,
    'encryptedEphemeralKey': e_b_b64
}

resp = requests.post(
    '{}/shares'.format(base_url),
    data=json.dumps(payload)
)



# shares should now have an entry for Bob 
resp = requests.get(
    '{}/shares'.format(base_url),
    params = {
        'filename': filename,
        'sender': pk_a_b64
    }
)


# DOWNLOAD

# Bob requests to download a file 
payload = {
    'filename': filename,
    'sender': pk_a_b64,
    'receiver': pk_b_b64,
}

resp = requests.post(
    '{}/download'.format(base_url),
    data=json.dumps(payload)
)

download_dict = resp.json()
e_b_b64 = download_dict['e_b']
edek_b_b64 = download_dict['edek_b']
c_b_b64 = download_dict['ciphertext']

e_b = decode_base64_str_into_bytes(e_b_b64)
edek_b = decode_base64_str_into_bytes(edek_b_b64)
c_b = decode_base64_str_into_bytes(c_b_b64)


emphermeral_key_b = pre.decrypt(sk_b, e_b)
dek_b = pre.decrypt(emphermeral_key_b, edek_b)
msg_b = pyaes.AESModeOfOperationCTR(dek_b).decrypt(c_b)

ipdb.set_trace()













