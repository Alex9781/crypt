from spellchecker import SpellChecker

alph = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
alph = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

f = open("C:\\Users\\alexz\\Desktop\\Univer\\2.1\\crypt\\out.txt", "w", encoding="utf-8")

spell = SpellChecker(language='ru')
words = []
sumcount = 0

for i in range(0, len(alph)):
    for j in range(0, len(alph)):
        for k in range(0, len(alph)):
            for l in range(0, len(alph)):
                for m in range(0, len(alph)):

                    key = str().join([alph[i], alph[j], alph[k], alph[l], alph[m]])
                    key = str(key)
                    if key.find(alph[i]) == key.rfind(alph[i]) and key.find(alph[j]) == key.rfind(alph[j]) and key.find(alph[k]) == key.rfind(alph[k]) and key.find(alph[l]) == key.rfind(alph[l]) and key.find(alph[m]) == key.rfind(alph[m]):
                        words.append(alph[i] + alph[j] + alph[k] + alph[l] + alph[m])
                        #f.write(alph[i] + alph[j] + alph[k] + alph[l] + alph[m] + ' ')

                    sumcount += 1


# knownWords = spell.known(words)

# for i in range(0, len(knownWords)):
#     f.write(knownWords.pop() + ' ')

for i in words:
    f.write(i + ' ')

print(sumcount)