import os
from base64 import b64decode

def findHammingDistance(first, second): # Function to find hamming distances. Works with "this is a test" and "wokka wokka!!!" to return 37
    distance = 0
    for x, y in zip(first, second):
        distance += bin(x ^ y).count('1')
    return distance

def createGroups(data, groupSize): # function to split into equal groups
    groups = [data[i:i + groupSize] for i in range(0, len(data), groupSize) if i < len(data) - groupSize]
    return groups

def normalizedDistance(text, keySize): # Function to find normalized hamming distance with guessed key size
    groups = createGroups(b64decode(text), keySize) 
    blocks = [b64decode(text)[0:keySize], b64decode(text)[keySize:keySize * 2]]
    hamming_distances = [[findHammingDistance(block, x) for x in groups] for block in blocks][0]
    mean = sum(hamming_distances) / len(hamming_distances)
    normalized = mean / keySize
    return normalized

def findKeyIndex(xorStrings): # Count occurences in each string, and find the index of the maximum count
    counts = [sum(string.count(character) for character in 'etaoinshrdlu') for string in xorStrings]
    keyIndex = counts.index(max(counts))
    return chr(keyIndex)

def findXorKey(data): # xor to find the vignere cipher key
    xorBytes = [[x ^ ord(character) for x in data] for character in [chr(x) for x in range(128)]] # ASCII range
    xorStrings = [''.join(list(map(chr, x))) for x in xorBytes]
    key = findKeyIndex(xorStrings)
    return key

def findBestKeySize(data):
    normalizeDistances = [{'keySize': keySize, 'distance': normalizedDistance(data, keySize)} for keySize in list(range(2, 41))] # Range of Key Combination from 2 to 40
    sorting = sorted(normalizeDistances, key=lambda x: x.get('distance'))
    keys = sorting[0].get('keySize')
    return keys

def transposeBlock(data, size): # transpose data by found specific size
    groups = createGroups(b64decode(data), size)
    transposedBlocks = list(zip(*groups))
    return transposedBlocks

def vKey(data): # Attempting to find the best vignere cipher key
    vKey = "".join(findXorKey(x) for x in transposeBlock(data, findBestKeySize(data)))
    return vKey

def decryptCipher(cipherData, key): # Function to decrypt ciphertext with given cipher data and key
    byteKey = bytearray.fromhex(key.encode('utf-8').hex())
    decryptBytes = [x ^ byteKey[i % len(byteKey)] for i, x in enumerate(b64decode(cipherData))]
    decryptedData = "".join([chr(x) for x in decryptBytes])
    return decryptedData

def breakingCipher(): # Bringing it together
    filePath = os.path.join(os.path.dirname(__file__), 'C1S6.txt') 
    cipherData = open(filePath).read()
    key = vKey(cipherData)
    decryptedCipher = decryptCipher(cipherData, key)
    return(key, decryptedCipher)

def main():
    key, decryptedCipher = breakingCipher()
    print("Decrypted Cipher Data using repeating key:", decryptedCipher, "\n", "Repeating Key is:", "\"", key, "\"")

if __name__ == "__main__":
    main()