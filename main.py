import itertools

cipher = input("Cipher: ").lower() or ""
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


functions = [(reverse,), (atbash,)]
for x in range(1, len(alphabet)):
    functions.append((caesar, x))

for r in range(1, 8):
    print("==", r, "==")
    rs = set()
    for x in itertools.combinations_with_replacement(functions, r):
        string = cipher
        for y in x:
            string = y[0](string, *y[1:])
        rs.add(string)
    rs = sorted(rs, key=lambda x: sum(len(y) for y in words if y in x))
    print(*rs[-3:][::-1], sep="\n")
