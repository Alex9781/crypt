from spellchecker import SpellChecker

def add2(add1, add2, param):
    res = 0
    if (param == 0):
        res = add1 + add2
    elif (param == 1):
        res = add1 - add2
    return res%lenn


def add3(add1, add2, add3, param):
    res = 0
    if (param == 0):
        res = add1 + add2 + add3
    elif (param == 1):
        res = add1 + add2 - add3
    elif (param == 2):
        res = add1 - add2 + add3
    elif (param == 3):
        res = add1 - add2 - add3
    return res%lenn


def add4(add1, add2, add3, add4, param):
    res = 0
    if (param == 0):
        res = add1 + add2 + add3 + add4
    elif (param == 1):
        res = add1 + add2 + add3 - add4
    elif (param == 2):
        res = add1 + add2 - add3 + add4
    elif (param == 3):
        res = add1 + add2 - add3 - add4
    elif (param == 4):
        res = add1 - add2 + add3 + add4
    elif (param == 5):
        res = add1 - add2 + add3 - add4
    elif (param == 6):
        res = add1 - add2 - add3 + add4
    elif (param == 7):
        res = add1 - add2 - add3 - add4
    return res%lenn


def add5(add1, add2, add3, add4, add5, param):
    res = 0
    if (param == 0):
        res = add1 + add2 + add3 + add4 + add5
    elif (param == 1):
        res = add1 + add2 + add3 + add4 - add5
    elif (param == 2):
        res = add1 + add2 + add3 - add4 + add5
    elif (param == 3):
        res = add1 + add2 + add3 - add4 - add5
    elif (param == 4):
        res = add1 + add2 - add3 + add4 + add5
    elif (param == 5):
        res = add1 + add2 - add3 + add4 - add5
    elif (param == 6):
        res = add1 + add2 - add3 - add4 + add5
    elif (param == 7):
        res = add1 + add2 - add3 - add4 - add5
    elif (param == 8):
        res = add1 - add2 + add3 + add4 + add5
    elif (param == 9):
        res = add1 - add2 + add3 + add4 - add5
    elif (param == 10):
        res = add1 - add2 + add3 - add4 + add5
    elif (param == 11):
        res = add1 - add2 + add3 - add4 - add5
    elif (param == 12):
        res = add1 - add2 - add3 + add4 + add5
    elif (param == 13):
        res = add1 - add2 - add3 + add4 - add5
    elif (param == 14):
        res = add1 - add2 - add3 - add4 + add5
    elif (param == 15):
        res = add1 - add2 - add3 - add4 - add5
    return res%lenn


alph = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
alph = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

lenn = len(alph)

f = open("C:\\Users\\alexz\\Desktop\\Univer\\2.1\\crypt\\out.txt", "w", encoding="utf-8")

spell = SpellChecker(language='ru')
words = []

for i in range(0, len(alph)):
    for j in range(0, 2):
        for k in range(0, 4):
            for l in range(0, 8):
                for m in range(0, 16):
                    words.append(alph[i] + alph[add2(i, 6, j)] + alph[add3(i, 6, 11, k)] + alph[add4(i, 6, 11, 3, l)] + alph[add5(i, 6, 11, 3, 8, m)])

words.sort()

knownWords = spell.known(words)
for i in range(0, len(knownWords)):
    f.write(knownWords.pop() + ' ')
