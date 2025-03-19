import string


def create_polybius_square(key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))
    key = key.replace("j", "i")
    alphabet = string.ascii_uppercase.replace("J", "")
    used_chars = list(key)
    for char in alphabet:
        if char not in used_chars:
            used_chars.append(char)
    keys = []
    for i in range(5):
        keys.append(used_chars[i * 5:(i + 1) * 5])
    return keys


def find_element_index(matrix, element):
    for i, row in enumerate(matrix):
        if element in row:
            return i, row.index(element)
    return None


def chopper2(worda):
    tmp = []
    i = 0
    while i < len(worda) - 1:
        tmp.append([worda[i], worda[i + 1]])
        i += 2
    return tmp


def encrypt(worda, keys):

    worda = word_fixer(worda)
    tmp = chopper2(worda)
    tmp2 = []
    for xs in tmp:
        fl = find_element_index(keys, xs[0])
        sl = find_element_index(keys, xs[1])

        if fl[0] == sl[0]:
            tmp2.append([keys[fl[0]][(fl[1] + 1) % 5], keys[sl[0]][(sl[1] + 1) % 5]])
        elif fl[1] == sl[1]:
            tmp2.append([keys[(fl[0] + 1) % 5][fl[1]], keys[(sl[0] + 1) % 5][sl[1]]])
        else:
            tmp2.append([keys[fl[0]][sl[1]], keys[sl[0]][fl[1]]])
    encrypted_word = ''.join([item[0] + item[1] for item in tmp2])
    return encrypted_word


def decrypt(worda, keys):
    worda = word_fixer(worda)
    tmp = chopper2(worda)
    tmp2 = []
    for xs in tmp:
        fl = find_element_index(keys, xs[0])
        sl = find_element_index(keys, xs[1])

        if fl[0] == sl[0]:
            tmp2.append([keys[fl[0]][(fl[1] - 1) % 5], keys[sl[0]][(sl[1] - 1) % 5]])
        elif fl[1] == sl[1]:
            tmp2.append([keys[(fl[0] - 1) % 5][fl[1]], keys[(sl[0] - 1) % 5][sl[1]]])
        else:
            tmp2.append([keys[fl[0]][sl[1]], keys[sl[0]][fl[1]]])

    encrypted_word = ''.join([item[0] + item[1] for item in tmp2])
    return encrypted_word


def word_fixer(worda):
    i = 0
    if len(worda) % 2 == 1:
        worda += "X"
    while i < len(worda) - 1:
        if worda[i] == worda[i + 1]:
            worda = worda[:i + 1] + "X" + worda[i + 1:]
            i += 2
        else:
            i += 1
    if len(worda) % 2 == 1:
        worda += "X"
    return worda


word = input("Enter word/phrase: ").split(" ")
k = input("Enter key: ").split(" ")
key_array = create_polybius_square(k)
tmp23 = ""
g = 0
for x in word:
    tmp23+= encrypt(x.upper(), key_array) + " "
    g+=1
g=0
tmp24 = tmp23.split(" ")
tmp25 = ""
for x in tmp24:
    tmp25+= decrypt(x.upper(), key_array) + " "
    g+=1

print('Encrypted Message; '+tmp23)
print('Decrypted Message: '+tmp25)
