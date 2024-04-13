import os
import base64
from Crypto.Cipher import AES

def decryptAESECB(encryptedData, key): # Function to decrypt a set of data using a specifying key
    decryptedData = AES.new(key, AES.MODE_ECB).decrypt(encryptedData) # Using PyCryptodome package, AES.MODE_ECB=1
    return decryptedData

def main():
    rawDataFile = open(os.path.join(os.path.dirname(__file__), 'C1S7.txt')).read() # Open file for raw data
    encryptedData = base64.b64decode(rawDataFile) # We know raw data in the file was Base64 encoded. Decode it into encrypted data.
    key = b'YELLOW SUBMARINE' # key was given
    decryptedData = decryptAESECB(encryptedData, key) # Use given data that has been Base64 decoded and given key
    print(decryptedData.decode('utf-8'))

if __name__ == "__main__":
    main()