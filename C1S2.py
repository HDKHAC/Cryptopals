import binascii

# Inputs
buffer1_hex_string = "1c0111001f010100061a024b53535009181c"
buffer2_hex_string = "686974207468652062756c6c277320657965"

def xor_buffers(buffer1_hex_string, buffer2_hex_string):
    # Check hex string for even length
    if len(buffer1_hex_string) % 2 != 0 or len(buffer2_hex_string) % 2 != 0:
        raise ValueError("One of the hexadecimal strings is Odd-length. Hex string must contain an even number of hex digits.")

    # hex string > bytes
    buffer1_rawb = binascii.unhexlify(buffer1_hex_string)
    buffer2_rawb = binascii.unhexlify(buffer2_hex_string)

    # Check buffer length
    if len(buffer1_rawb) != len(buffer2_rawb):
        raise ValueError("Buffers are not of equal length. For this function, they needs to be equal length.")

    # XOR the two buffers by iterate through tuples
    xor_rawb = bytes(x ^ y for x, y in zip(buffer1_rawb, buffer2_rawb))

    # bytes > hex string
    xor_hex_string = binascii.hexlify(xor_rawb).decode('utf-8')

    return xor_hex_string

xor_hex_string = xor_buffers(buffer1_hex_string, buffer2_hex_string)

print(xor_hex_string)
