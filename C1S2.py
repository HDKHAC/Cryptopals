# Inputs
buffer1_hex_string = "1c0111001f010100061a024b53535009181c"
buffer2_hex_string = "686974207468652062756c6c277320657965"

def xor_buffers(buffer1_hex_string, buffer2_hex_string):
    # hex string > bytes
    buffer1_rawb = bytes.fromhex(buffer1_hex_string)
    buffer2_rawb = bytes.fromhex(buffer2_hex_string)
    # XOR the two buffers by iterate through tuples
    xor_rawb = bytes(x ^ y for x, y in zip(buffer1_rawb, buffer2_rawb))
    # bytes > hex string
    xor_hex_string = xor_rawb.hex()
    return xor_hex_string

xor_hex_string = xor_buffers(buffer1_hex_string, buffer2_hex_string)
print(xor_hex_string)