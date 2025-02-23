def dzielniki(liczba):
    dziel = []
    x = liczba
    while x > 0:
        if liczba % x == 0:
            dziel.append(x)
        x -= 1
    return dziel

def dzielniki2(liczba):
    dziel = []
    x = liczba // 2
    while x > 0:
        if liczba % x == 0:
            dziel.append(x)
        x -= 1
    return dziel

#print(dzielniki(10))

def nwd(l1, l2):
    wspolne = []
    dziel1 = dzielniki(l1)
    dziel2 = dzielniki(l2)

    for x in dziel1:
        for y in dziel2:
            if x == y:
                wspolne.append(x)
    if len(wspolne) == 1:
        return True
    return False

#print(nwd(3, 5))

def zad_16_1():
    ile = 0
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\16\liczby16.txt", "r")
    liczby_txt = plik.readlines()
    liczby = []
    for x in liczby_txt:
        liczby.append(int(x))
    for x in liczby:
        for y in liczby:
            #print(y)
            if nwd(x, y):
                ile += 1
    print(ile // 2)


def zad_16_2():
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\16\liczby16.txt", "r")
    liczby_txt = plik.readlines()
    liczby = []
    for x in liczby_txt:
        liczby.append(int(x))
    for x in liczby:
        if len(dzielniki(x)) == 9:
            print(x)

def zad_16_3():
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\16\liczby16.txt", "r")
    liczby_txt = plik.readlines()
    liczby = []
    for x in liczby_txt:
        liczby.append(int(x))
    for x in liczby:
        d = dzielniki2(x)
        suma = 0
        for y in d:
            suma += y
        if suma == x:
            print(x)

zad_16_3()

