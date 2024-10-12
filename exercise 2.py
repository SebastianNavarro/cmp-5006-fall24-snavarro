# Suppose that APNDJI or XYGROBO are ciphertexts that are obtained from encryption using the Shift Cipher. Show in each case that there are two ”meaningful” plaintexts that could encrypt to the given ciphertext. 

# Shift Cipher
def shift_cipher_forward(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

def shift_cipher_backward(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97)
    return result

def brute_force(text):
    print("Forward:")
    for i in range(1, 26):
        print(f"Shift {i}: {shift_cipher_forward(text, i)}")
    print("\nBackward:")
    for i in range(1, 26):
        print(f"Shift {i}: {shift_cipher_backward(text, i)}")

cypher_text = "XYGROBO"
brute_force(cypher_text)