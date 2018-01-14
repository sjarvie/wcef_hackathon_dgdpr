/*
Declare Alice's keys
sk_a = b'\x00\n\x8b\xeb\xc31\x81\x06\xbb\xb8\x92\xa5\x9dO7\xc7\xd1\xcc\x98\xbdM5\xbd\x13\xd9\xb9\x84\xea\xd6\x8e\x89H\xe0'
sk_a_b64 = encode_bytes_to_base_64_str(sk_a) # 'AAqL68MxgQa7uJKlnU83x9HMmL1NNb0T2bmE6taOiUjg'

pk_a = b'\x01\x02b\xaa<\xf9\xa2\xe0\xfb\x7f\xaf`\xaa\xc0\xf6l\x8a]h\xfb\xe3\x06\xc9\xd3\xf0\xbf~\\\xe7w+\xea\xf6%'
pk_a_b64 = encode_bytes_to_base_64_str(pk_a) # 'AQJiqjz5ouD7f69gqsD2bIpdaPvjBsnT8L9+XOd3K+r2JQ=='


# Declare Bob's keys
sk_b = b"\x00\x030'\xac\xf1 \x913\x0f\xc2\xbf\xfb*\xb53\x8b\xf0\xb6\r[`\x1bM\xc8\xb6\xd5$\x9d2k\xb4\xc7"
sk_b_b64 = encode_bytes_to_base_64_str(sk_b) #  'AAMwJ6zxIJEzD8K/+yq1M4vwtg1bYBtNyLbVJJ0ya7TH'

pk_b = b'\x01\x02k\x1c{d\xc8Q!\xf9-&\xde\x93\xf7\xf6HqgM\xb8\xf9o\xd1_q4R\xcb-\xb3j\x93\xc0'
pk_b_b64 = encode_bytes_to_base_64_str(pk_b) # 'AQJrHHtkyFEh+S0m3pP39khxZ024+W/RX3E0Ussts2qTwA=='
 */

module.exports = {
  base_url: 'http://edwards-mbp:8000',

  alice: {
    sk_b64: 'AAqL68MxgQa7uJKlnU83x9HMmL1NNb0T2bmE6taOiUjg',
    pk_b64: 'AQJiqjz5ouD7f69gqsD2bIpdaPvjBsnT8L9+XOd3K+r2JQ=='
  },

  bob: {
    sk_b64: 'AAMwJ6zxIJEzD8K/+yq1M4vwtg1bYBtNyLbVJJ0ya7TH',
    pk_b64: 'AQJrHHtkyFEh+S0m3pP39khxZ024+W/RX3E0Ussts2qTwA=='
  }
};
