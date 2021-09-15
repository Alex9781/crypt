def bellaso_decrypt(msg, key):
    ''' INPUT: str (encrypted), key (used w tabula recta to decrypt)
        OUTPUT: str (decrypted)
    '''
    decrypted = ''
    alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    offset = 0
    # for-loop over every position in the message
    for ix in range(len(msg)):
        # and if it's not an alpha w correspondence
        if msg[ix] not in alph:
            # just return the original character (whitespace or punctuation)
            output = msg[ix]
            # increment var to reflect offset that this step creates over time
            offset += -1
        # otherwise if the position wraps longer than len(alpha),
        elif (alph.find(msg[ix])) > (len(alph) - 
                            # modulo to get proper position in alphabet key
                            (alph.find(key[((ix + offset) % len(key))])) - 1):
            # then check to get our corresponding letter based on keyword
            output = alph[(alph.find(msg[ix]) - 
                            (alph.find(key[((ix + offset) % len(key))]))) % len(alph)]
        # else is same as previous case, but no wrapping so no modulo operation
        else:
            output = alph[alph.find(msg[ix]) - 
                                (alph.find(key[((ix + offset) % len(key))]))]
        # put it all together and
        decrypted += output
    # what does that spell?
    return decrypted
# hooray!

msd = "мхлщлифцбдюгишсптаивпбьдюолдьуэюыйемхл"

f = open("C:\\Users\\alexz\\Desktop\\Univer\\2.1\\crypt\\out.txt", "r", encoding="utf-8")
f1 = open("C:\\Users\\alexz\\Desktop\\Univer\\2.1\\crypt\\out1.txt", "w", encoding="utf-8")

frases = []

key = f.read().split(' ')

for i in range(0, len(key) - 1):
    frases.append(bellaso_decrypt(msd, key.pop(0)))

frases.sort()

for i in frases:
    i = str(i)
    j = i[0]
    k = i[19]
    if j == k and 'ыъьй'.find(j) == -1:
        f1.write(i[0:19] + '\n')

# for i in frases:
#     f1.write(i + '\n')