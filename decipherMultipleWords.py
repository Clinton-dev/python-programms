"""
Write a function that takes a string and returns and returns the deciphered string so that you can show the commander that the minions are talking about “Lance & Janice” instead of doing their jobs.
did you see last night's episode?
Yeah! I can't believe Lance lost his job at the colony!!
"""


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
