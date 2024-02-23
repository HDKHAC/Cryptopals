import binascii
import base64

# hex
hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

# hex > raw bytes
rawb = binascii.unhexlify(hex_string)
print(rawb)

# raw bytes > base64
base64b = base64.b64encode(rawb)
print(base64b)

# base64 > string
base64s = base64b.decode('utf-8')
print(base64s)
