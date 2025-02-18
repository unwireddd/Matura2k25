
def sprawdz01(liczba):
    zera = 0
    jedynki = 0
    liczba2 = int(liczba)
    znaki = []
    while int(liczba2) > 0:
        znaki.append(liczba2 % 2)
        liczba2 = liczba2 // 2
    for x in range(len(znaki)):
        if znaki[x] == 0:
            zera += 1
        else:
            jedynki += 1
    if zera == jedynki:
        return True
    return False

def zamien(liczba, baza):
    zera = 0
    jedynki = 0
    liczba2 = int(liczba)
    znaki = []
    while int(liczba2) > 0:
        znaki.append(liczba2 % baza)
        liczba2 = liczba2 // baza
    return znaki

def zad_13_1():
    licznik = 0
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\13\liczby13.txt", "r")
    liczby = plik.readlines()
    for x in liczby:
        if sprawdz01(x):
            licznik += 1
    print(licznik)

def zad_13_2():
    konwersje = {}
    licznik = 0
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\13\liczby13.txt", "r")
    liczby = plik.readlines()
    max = 0
    for x in liczby:
        licznik = 0
        konwersje[x] = zamien(x,5)
        for y in konwersje[x]:
            if y == 4:
                licznik += 1
        if licznik > max:
            max = licznik
    for x in konwersje:
        licznik = 0
        for y in konwersje[x]:
            if y == 4:
                licznik += 1
        if licznik == max:
            print(x)

    pass

def zad_13_3():
    pass

#zad_13_1()
zad_13_2( )
#zad_13_3()
