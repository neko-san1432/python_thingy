def railFenceEncrypt(plaintext, depth):
    if depth == 1:
        return plaintext

    rail = ['' for _ in range(depth)]
    row, step = 0, 1

    for char in plaintext:
        rail[row] += char
        if row == 0:
            step = 1
        elif row == depth - 1:
            step = -1
        row += step

    return ''.join(rail)


def railFenceDecrypt(ciphertext, depth):
    if depth == 1:
        return ciphertext

    rail = [['\n' for _ in range(len(ciphertext))] for _ in range(depth)]

    direction_down = None
    row, col = 0, 0

    for _ in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == depth - 1:
            direction_down = False

        rail[row][col] = '*'
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(depth):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1

    result = []
    row, col = 0, 0
    for _ in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == depth - 1:
            direction_down = False

        result.append(rail[row][col])
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    return ''.join(result)


# Example usage:
depth = int(input("Input depth: "))
text = input("Input text: ")

encrypted_text = railFenceEncrypt(text, depth)
print(f"Encrypted: {encrypted_text}")

decrypted_text = railFenceDecrypt(encrypted_text, depth)
print(f"Decrypted: {decrypted_text}")
