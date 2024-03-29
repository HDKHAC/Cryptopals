from binascii import hexlify

text = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"
def encrypting(text, key):
  textBytes = text.encode()
  keyBytes = key.encode()
  encryptedBytes = bytes([textBytes[i] ^ keyBytes[i % len(keyBytes)] for i in range(len(textBytes))])
  return hexlify(encryptedBytes).decode("utf-8")

encryptedText = encrypting(text, key)
print(encryptedText)