import itertools
from multiprocessing import Pool

cipher = input("Cipher: ").upper() or ""
alphabet = input("Alphabet [A-Z]: ").upper() or "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
words = [x.strip("\n").upper() for x in open(input("Dictionary [words.txt]: ") or "words.txt", "r").readlines()]
keys = [x.strip("\n").upper() for x in open(input("Keys [keys.txt]: ") or "keys.txt", "r").readlines()]


def reverse(string):
    return string[::-1]


def replace(string, salphabet):
    return "".join([salphabet[alphabet.index(x)] if x in alphabet else x for x in string])


def caesar(string, shift):
    return replace(string, alphabet[shift:] + alphabet[:shift])


def atbash(string):
    return replace(string, alphabet[::-1])


def vigenere_enc(string, key):
    key = [x for x in key.upper() if x in alphabet]
    i = 0
    estring = ""
    for char in string:
        if char in alphabet:
            char = caesar(char, alphabet.index(key[i % len(key)]))
            i += 1
        estring += char
    return estring


def vigenere_dec(string, key):
    key = [x for x in key.upper() if x in alphabet]
    i = 0
    estring = ""
    for char in string:
        if char in alphabet:
            char = alphabet[caesar(alphabet, alphabet.index(key[i % len(key)])).index(char)]
            i += 1
        estring += char
    return estring


functions = [(reverse,), (atbash,)]
for x in range(1, len(alphabet)):
    functions.append((caesar, x))
for x in keys:
    functions.append((vigenere_dec, x))
    #functions.append((vigenere_enc, x))


def calculate_cipher(x):
    string = cipher
    for y in x:
        string = y[0](string, *y[1:])

    info = tuple((x1[0].__name__, *x1[1:]) for x1 in x)

    val = sum(len(y) for y in words if y in string)

    return string, info, val

p = Pool(4)

for r in range(1, 8):
    print("==", r, "==")
    rs = sorted(
        filter(
            lambda x: x[0] != cipher,
            p.map(
                calculate_cipher,
                itertools.combinations_with_replacement(functions, r)
            )
        ),
        key=lambda x: x[2]
    )
    print(*rs[-6:][::-1], sep="\n")
