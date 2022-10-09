def decipherOneWord(text):
    encrypt = 'abcdefghijklmnopqrstuvwxyz'
    word = [letter for letter in text]

    for index, character in enumerate(word):
        character_index = encrypt.find(character)
        decrypt_index = 25 - character_index
        if character.islower():
            word[index] = encrypt[decrypt_index]

    return ''.join(word)


def decipherMultipleWords(text):
    words = text.split()
    for index, word in enumerate(words):
        words[index] = decipherOneWord(word)

    return ' '.join(words)


print(decipherMultipleWords("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
print(decipherMultipleWords(
    "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))
