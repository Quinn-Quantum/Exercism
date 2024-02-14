import string
def rotate(text, key):
    encrypted = ""
    for c in text:
        if c in string.ascii_uppercase:
            encrypted += chr((ord(c) - ord('A') +  key) % 26 + ord('A'))
        elif c in string.ascii_lowercase:
            encrypted += chr((ord(c) - ord('a') +  key) % 26 + ord('a'))
        else:
            encrypted += c
    return encrypted
    
