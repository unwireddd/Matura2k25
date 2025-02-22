def czyPierwsza(liczba):
    x = 2
    if liczba < 2:
        return False
    while x < liczba:
        if liczba % x == 0:
            return False
        x += 1
    return True

def czySuperpierwsza(liczba):
    cyfry = []
    suma = 0
    while liczba > 0:
        cyfry.append(liczba % 10)
        liczba = liczba // 10

    for x in cyfry:
        suma += x
    return czyPierwsza(suma)


def czyBSuperpierwsza(liczba):
    cyfry = []
    suma = 0
    while liczba > 0:
        cyfry.append(liczba % 2)
        liczba = liczba // 2

    for x in cyfry:
        suma += x
    return czyPierwsza(suma)





def zad_15_1():
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\15\liczby15.txt", "r")
    liczby_txt = plik.readlines()
    liczby = []
    licz = 0
    for x in liczby_txt:
        liczby.append(int(x))
    for x in liczby:
        if czyPierwsza(x):
            licz += 1
    print(licz)

def zad_15_2():
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\15\liczby15.txt", "r")
    liczby_txt = plik.readlines()
    liczby = []
    licz = []
    for x in liczby_txt:
        liczby.append(int(x))
    for x in liczby:
        if czyPierwsza(x) and czySuperpierwsza(x) and czyBSuperpierwsza(x):
            licz.append(x)

    licz.sort()
    print(licz)

def zad_15_3():
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\15\liczby15.txt", "r")
    liczby_txt = plik.readlines()
    liczby = []
    pierwsze = []
    for x in liczby_txt:
        liczby.append(int(x))
    for x in liczby:
        if czyPierwsza(x):
            pierwsze.append(x)
    pierwsze.sort()
    for x in range(1, len(pierwsze)):
        if pierwsze[x] - pierwsze[x - 1] == 2:
            print(f"[{pierwsze[x]}, {pierwsze[x - 1]}]")



#zad_15_1()
#zad_15_2()
zad_15_3()
