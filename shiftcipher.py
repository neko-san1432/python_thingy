import string
import nltk
from nltk.corpus import words
alpha_big = list(string.ascii_uppercase)
alpha_small = list(string.ascii_lowercase)
nltk.download('words')
valid_words = set(words.words())
tmp4 = []




def encrypt(text, shiftI):
    tmp = []
    tmp2 = chopper(text)
    for i in tmp2:
        tmp3 = ""
        for j in i:
            if findsSmall(j) != -1:
                tmp3 += alpha_small[(findsSmall(j)+shiftI)%26]
            elif findBig(j) != -1:
                tmp3 += alpha_big[(findBig(j) + shiftI)%26]
            else:
                tmp3+=j
        tmp.append(tmp3)
    return " ".join(tmp)


def decrypt(cip_text):
    tmp =[]
    n=1
    tmp5 = chopper(cip_text)
    while n!=26:
        for i in tmp5:
            tmp3 = ""
            for j in i:
                if findsSmall(j) != -1:
                    tmp3 += alpha_small[(findsSmall(j) - n)%26]
                elif findBig(j) != -1:
                    tmp3 += alpha_big[(findBig(j) - n)%26]
                else:
                    tmp3 += j
            tmp.append(tmp3)
        if is_valid_word(tmp[0]):
            return "["+str(n)+"]"+ " ".join(tmp)
        tmp=[]
        n+=1


def findsSmall(letter):
    try:
        return alpha_small.index(letter)
    except Exception as e:
        # print(e)
        return -1

def findBig(letter):
    try:
        return alpha_big.index(letter)
    except Exception as e:
        # print(e)
        return -1

def chopper(text):
    ey = text.split()
    return ey




def is_valid_word(word):
    return word.lower() in valid_words

print("Encrypt text:")
print(encrypt("Phone linging, pick up your phone big boy",3))
print("Decrypt text:")
print(decrypt(encrypt("Phone linging, pick up your phone big boy",3)))
print("Decrypt text:")
print(decrypt("WUDLQLQJ PDNHV SHUIHFW"))
print("Decrypt another text:")
print(decrypt("WKLQNLQJ LV WKH NHB WR VXFFHVV"))


