
##### 
####  This script implements RC4 cryptographic algorithm  
####



def KSA(key):
    key = [ord(c) for c in key]
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S):
    i = 0
    j = 0
    while True :    
        i = (i+1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap
        K = S[(S[i] + S[j]) % 256]
        yield K   # generate next byte

def rc4(key, data):
    S = KSA(key)
    keystream = PRGA(S)
    return bytes([c ^ next(keystream) for c in data])

ciphertext = rc4("secret", b"hello world")
plaintext = rc4("secret", ciphertext)
print(ciphertext)
print(plaintext)

