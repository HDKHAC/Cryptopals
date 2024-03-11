hexString = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736' # Global variable for input hex encoded string
def scoreDecryptedText(decryptedText):   # Function to score decrypted results
    alphabetWeight = {'E': .90, 'T': 0.90, 'A': 0.90, 'O': 0.90, 'I': 0.90, 'N': 0.90, 'S': 0.60, 'R': 0.60, 'H': 0.60, 'D': 0.60, 'L': 0.60, 'U': 0.60, # Higher weight based on hint ETAOIN SHRDLU
                      'B': 0.35, 'C': 0.35, 'F': 0.35, 'G': 0.35, 'J': 0.35, 'K': 0.35, 'M': 0.35, 'P': 0.35, 'Q': 0.35, 'V': 0.35, 'W': 0.35, 'X': 0.35, 'Y': 0.35, 'Z': 0.35}  # Lower weight based on hint given "ETAOIN SHRDLU"
    decryptedText = decryptedText.upper() # All be in upper case for simplicity
    if '  ' in decryptedText:    # Check for double spaces and apply 0 score
        return 0
    # Check for consecutive vowels and consonants in first 4 letters to sense first valid first word and apply multiplier
    countVowels, countConsonants = 0, 0
    for i in range(4):
        if decryptedText[i] in 'AEIOU':
            countVowels += 1
            countConsonants = 0
        else:
            countConsonants += 1
            countVowels = 0
    if countVowels >= 3 or countConsonants >= 4: # First 4 letters beginning with 3 consecutive vowels or 4 consecutive consonants
        return sum(alphabetWeight.get(points, 0) for points in decryptedText) * 0.3 # Decreased multiplier
    else:
        return sum(alphabetWeight.get(points, 0) for points in decryptedText) # No multiplier

def findDecryptedText():
    rawBytes = bytes.fromhex(hexString)
    decryptedResults = []   # Place to store decrypted data
    for keyCharacter in range(97, 123):   # XOR with ASCII values for lowercase letters: a-z
        result = bytes([byte ^ keyCharacter for byte in rawBytes])
        result = result.replace(b'\x00', b' ')  # Replace null bytes with space
        result = bytes([byte if 97 <= byte <= 122 or 65 <= byte <= 90 else 32 for byte in result])  # Filter out ASCII control characters, expressions, and extended, etc.
        decryptedText = result.decode('utf-8')
        decryptedTextScore = scoreDecryptedText(decryptedText)   # Scoring the decrypted text based on hardcoded weights and multipliers
        decryptedResults.append((decryptedText, decryptedTextScore, keyCharacter))
    decryptedResults.sort(key=lambda x: x[1], reverse=True) # Sorting the decrypted results based on score (decryptedTextScore)
    print("Based on given hex encoded string message:", hexString)
    for decryptedText, decryptedTextScore, keyCharacter in decryptedResults[:3]: # Top 3 decrypted results
        print(f"Decrypted message: {decryptedText.upper()}, Score: {decryptedTextScore}, Using Key Character: {chr(keyCharacter)}")
    decryptedText, decryptedTextScore, keyCharacter = decryptedResults[0]    # Number 1 decrypted results
    print(f"\nMessage with the highest score: {decryptedText.upper()}\nCharacter with the highest score: {chr(keyCharacter)}")

def main():
    findDecryptedText()
if __name__ == "__main__":
    main()