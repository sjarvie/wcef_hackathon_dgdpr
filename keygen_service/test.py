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




s_k = b'\x00\n\x8b\xeb\xc31\x81\x06\xbb\xb8\x92\xa5\x9dO7\xc7\xd1\xcc\x98\xbdM5\xbd\x13\xd9\xb9\x84\xea\xd6\x8e\x89H\xe0'
s_k_b64 = encode_bytes_to_base_64_str(s_k)

p_k = b'\x01\x02b\xaa<\xf9\xa2\xe0\xfb\x7f\xaf`\xaa\xc0\xf6l\x8a]h\xfb\xe3\x06\xc9\xd3\xf0\xbf~\\\xe7w+\xea\xf6%'
p_k_b64 = encode_bytes_to_base_64_str(p_k)

base_url = 'http://localhost:8889'


p_k_encoded = encode_bytes_to_base_64_str(p_k)

data = 'Some data that we are hiding'
data_b64 = encode_bytes_to_base_64_str(str.encode(data))




# ---- TEST GEN PRIV

'{}/nucypher_test_handler'.format(base_url),
ephemeral_key = requests.get('{}/gen_priv'.format(base_url)).text


# TEST RECRYPT
payload = {
    'sk_in': s_k_b64,
    'sk_out': ephemeral_key
}

r = requests.post(
    '{}/rekey'.format(base_url),
    data=json.dumps(payload)
)
re_ab = r.text


# TEST ENCRYPT

payload = {
    'pk': p_k_b64,
    'data': data_b64
}

r = requests.post(
    '{}/encrypt'.format(base_url),
    data=json.dumps(payload)
)
c = r.text


# TEST DECRYPT

payload = {
    'sk': s_k_b64,
    'c': c
}

r = requests.post(
    '{}/decrypt'.format(base_url),
    data=json.dumps(payload)
)
data_dec = r.text

print(bytes.decode(decode_base64_str_into_bytes(data_dec)) == data)


# TEST ENCRYPT AES

dek = str(uuid.uuid4())[0:32]  # random symmetric key


payload = {
    'dek': dek,
    'data': data_b64
}

r = requests.post(
    '{}/encrypt_aes'.format(base_url),
    data=json.dumps(payload)
)
encrypted_data = r.text


# TEST DECRYPT AES

payload = {
    'dek': dek,
    'c': encrypted_data
}

r = requests.post(
    '{}/decrypt_aes'.format(base_url),
    data=json.dumps(payload)
)
decrypted_b64 = r.text
decrypted_data = decode_base64_str_into_bytes(decrypted_b64)

print(bytes.decode(decrypted_data) == data)













