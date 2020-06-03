import itertools

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


def vigenere(string, key):
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
    functions.append((vigenere, x))

for r in range(1, 8):
    print("==", r, "==")
    rs = set()
    for x in itertools.combinations_with_replacement(functions, r):
        string = cipher
        for y in x:
            string = y[0](string, *y[1:])
        rs.add((string,) + tuple((x1[0].__name__, *x1[1:]) for x1 in x))
    rs = sorted(rs, key=lambda x: sum(len(y) for y in words if y in x[0]))
    print(*rs[-3:][::-1], sep="\n")
