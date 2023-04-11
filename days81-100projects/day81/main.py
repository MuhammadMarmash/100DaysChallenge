user_input = input("Enter a sentence to convert to morse code: ")

morse_codes = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}


def sentence_to_morse(sentence):
    sentence = sentence.split(" ")
    for i in range(len(sentence)):
        for char in sentence[i]:
            sentence[i] = sentence[i].replace(char, morse_codes[char])

    sentence = ".....".join(sentence)
    print(sentence)


sentence_to_morse(user_input)
