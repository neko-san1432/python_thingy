def railFenceEncrypt(plaintext, dp):
    plaintext = spikeChecker(plaintext, dp)
    if dp == 1:
        return plaintext

    rail = ['' for _ in range(dp)]
    row, step = 0, 1

    for char in plaintext:
        rail[row] += char
        if row == 0:
            step = 1
        elif row == dp - 1:
            step = -1
        row += step

    return ''.join(rail)


def railFenceDecrypt(ciphertext, dpt):
    if dpt == 1:
        return ciphertext

    rail = [['\n' for _ in range(len(ciphertext))] for _ in range(dpt)]

    direction_down = None
    row, col = 0, 0

    for _ in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == dpt - 1:
            direction_down = False

        rail[row][col] = '*'
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(dpt):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1

    result = []
    row, col = 0, 0
    for _ in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == dpt - 1:
            direction_down = False

        result.append(rail[row][col])
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    return ''.join(result)


def spikeChecker(t, d):
    step_size = (d * 2) - 2
    current_index = d - 1
    try:
        while True:
            _ = t[current_index]
            current_index += step_size
    except IndexError:
        remaining_chars = (len(t) - 1) - current_index
        t += 'x' *(remaining_chars*-1)
        return t


# Example usage:
depth = int(input("Input depth: "))
text = input("Input text: ")

encrypted_text = railFenceEncrypt(text, depth)
print(f"Encrypted: {encrypted_text}")

decrypted_text = railFenceDecrypt(encrypted_text, depth)
print(f"Decrypted: {decrypted_text}")
