def zrownowazone():
    plik = open("/home/elliot/Downloads/DANE/DANE_E/anagram.txt", "r")
    linie_u = plik.readlines()
    ile = 0
    ile_p = 0
    linie = []
    for x in linie_u:
        linie.append(x[:-1])
    
    for linia in linie:
        cyfry = []
        zera = 0
        jedynki = 0
        #print(linie)
        for x in range(len(linia)):
            cyfry.append(int(linia[x]))
        for x in cyfry:
            if x == 0:
                zera += 1
            if x == 1:
                jedynki += 1
        if zera == jedynki:
            ile += 1
        elif zera == jedynki + 1 or zera == jedynki - 1:
            ile_p += 1
    
    print(ile)
    print(ile_p)

zrownowazone()
