def deszyfruj(tekst):
    nowy = []
    digits = set("23456789")
    for x in range(len(tekst)):
        if tekst[x] in digits:
            for y in range(int(tekst[x]) - 1):
                nowy.append(tekst[x - 1])
        else:
            nowy.append(tekst[x])
    print(nowy)

deszyfruj("F5A4CDM4")
