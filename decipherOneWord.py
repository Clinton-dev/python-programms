""" decipher one word """


def decipherOneWord(text):
    encrypt = 'abcdefghijklmnopqrstuvwxyz'
    word = [letter for letter in text]

    for index, character in enumerate(word):
        character_index = encrypt.find(character)
        decrypt_index = 25 - character_index
        word[index] = encrypt[decrypt_index]

    return ''.join(word)


print(decipherOneWord('abc'))
print(decipherOneWord('zyx'))
