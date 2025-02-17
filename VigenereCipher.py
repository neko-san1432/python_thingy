import string
alpha = list(string.ascii_uppercase)



def vig(text, keys):
    cipherText = ""

    keys = checker(text,keys)
    chopped_key = chopper(checker(text,keys.upper()))
    chopped_text = chopper(text.upper())
    for i, j in zip(chopped_text, chopped_key):
        if find(i) != -1:
            cipherText += alpha[(find(i) + find(j)) % 26]
        else:
            cipherText += i

    return cipherText,keys

def decipher(cip_text,keys):
    decipherText = ""
    keys = checker(cip_text, keys)
    chopped_key = chopper(checker(cip_text,keys.upper()))
    chopped_text = chopper(cip_text.upper())
    for i, j in zip(chopped_text, chopped_key):
        if find(i) != -1:
            decipherText += alpha[(find(i) - find(j)) % 26]
        else:
            decipherText += i
    return decipherText,keys

def find(letter):
    try:
        return alpha.index(letter)
    except Exception as e:
        return -1

def chopper(s):
    return [char for char in s if char.isalpha()]


def checker(text, keys):
    if len(text) <= len(keys):
        return keys
    else:
        tmp = 0
        tmp_key = keys
        while len(text) >= len(tmp_key):
            tmp_key+=keys[tmp]
            if tmp == len(keys)-1:
                tmp = 0
            else:
                tmp+=1
        return tmp_key

t,k = vig("CRYPTOGRAPHY IS FUN WHEN YOU UNDERSTAND THE PATTERNS ","SECURITY")
print("Cipher text : " + t+"\n"+"Key : "+k)
print("\n")
pt,k  = decipher(t,k)
print("Decipher text : " + pt+"\n"+"Key : "+k)
