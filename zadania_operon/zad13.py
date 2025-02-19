
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

def zad_13_2(baza):
    konwersje = {}
    licznik = 0
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\13\liczby13.txt", "r")
    liczby = plik.readlines()
    max = 0
    for x in liczby:
        licznik = 0
        konwersje[x] = zamien(x, baza)
        for y in konwersje[x]:
            if y == baza - 1:
                licznik += 1
        if licznik > max:
            max = licznik
    for x in konwersje:
        licznik = 0
        for y in konwersje[x]:
            if y == baza - 1:
                licznik += 1
        if licznik == max:
            print(x)

    pass

def zad_13_3(baza):
    konwersje = {}
    licznik = 0
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\13\liczby13.txt", "r")
    liczby = plik.readlines()
    max = 0
    for x in liczby:
        licznik = 0
        konwersje[x] = zamien(x, baza)
        tablica = konwersje[x]
        dlugosc = len(tablica)
        tab1 = tablica[:dlugosc // 2]
        tab2 = tablica[-(dlugosc - 1) // 2:]
        dlugosc2 = len(tab2) - 1
        tab3 = []
        for y in range(len(tab2)):
            tab3.append(y)
        for z in range(len(tab2)):
            tab3[dlugosc2] = tab2[z]
            dlugosc2 -= 1
        rowne = True
        for z in range(len(tab3)):
            if tab1[z] != tab3[z]:
                rowne = False
                break
        if rowne:
            print(x)




    pass

#zad_13_1()
#zad_13_2(5)
#zad_13_2(7)
#zad_13_2(13)
zad_13_3(16)
