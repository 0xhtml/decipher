import itertools
import base64

cipher = input("Cipher: ") or ""
alphabet = input("Alphabet [a-z]: ") or "abcdefghijklmnopqrstuvwxyz"
words = [x.strip("\n") for x in open(input("Dictionary [words.txt]: ") or "words.txt", "r").readlines()]


def reverse(string):
    return string[::-1]


def replace(string, salphabet):
    estring = ""
    for char in string:
        if char in alphabet:
            char = salphabet[alphabet.index(char)]
        estring += char
    return estring


def caesar(string, shift):
    return replace(string, alphabet[shift:] + alphabet[:shift])


def atbash(string):
    return replace(string, alphabet[::-1])


def b64e(string):
    return base64.b64encode(string.encode()).decode()


def b64d(string):
    try:
        return base64.b64decode(string).decode()
    except (base64.binascii.Error, UnicodeDecodeError):
        return string


functions = [(reverse,), (atbash,), (b64e,), (b64d,)]
for x in range(1, len(alphabet)):
    functions.append((caesar, x))

for r in range(1, 8):
    print("==", r, "==")
    for x in itertools.combinations_with_replacement(functions, r):
        string = cipher
        for y in x:
            string = y[0](string, *y[1:])
        i = 0
        j = 0
        for y in words:
            if y in string:
                i += len(y)
                j += 1
        if i/j > 2:
             print(string)
