def zad_24_1():
    numery = []
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\24\dane.txt", "r")
    dane = plik.readlines()
    for x in dane:
        numery.append(x[:3])
    mapa = {}
    for x in numery:
        if x in mapa:
            mapa[x] += 1
        else:
            mapa[x] = 1
    max = 0
    for x in mapa:
        if mapa[x] > max:
            max = mapa[x]
    for x in mapa:
        if mapa[x] == max:
            print(f"{x}: {max}")

def zad_24_2():
    imiona = []
    tab = {}
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\24\dane.txt", "r")
    dane = plik.readlines()

    for x in dane:
        imie = x.split(".")[1].upper()
        imiona.append(imie)
    for x in imiona:
        if x in tab:
            tab[x] += 1
        else:
            tab[x] = 1
    imiona = list(tab.keys())
    imiona.sort()

    max = 0
    for x in tab:
        if tab[x] > max:
            max = tab[x]
    for x in range(max, 0, -1):
        for imie in imiona:
            if tab[imie] == x:
                print(f"{imie}: {x}")


zad_24_2()