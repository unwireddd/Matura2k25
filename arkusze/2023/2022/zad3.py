import math

def czy_pierwsza(liczba):
    c = math.ceil(math.sqrt(liczba))
    for x in range(2, c + 1):
        #print(x)

        if liczba % x == 0:
            return False

    return True


def ile_pierwszych():
    plik = open("/home/elliot/Downloads/Dane_2212/liczby.txt", "r")
    liczby_str = plik.readlines()
    liczby = []
    ile = 0
    for x in liczby_str:
        liczby.append(int(x))

    for x in range(1, len(liczby)):
        if czy_pierwsza(liczby[x]-1):
            ile += 1
    print(ile)

def goldbach():
    rozklady = []
    plik = open("/home/elliot/Downloads/Dane_2212/liczby.txt", "r")
    liczby_str = plik.readlines()
    liczby = []
    ile = 0
    for x in liczby_str:
        liczby.append(int(x))

    pierwsze = {}
    for x in range(4, 1000001):
        print(f"spr {x}")
        if czy_pierwsza(x):
            pierwsze[x] = True

    lic = 1
    for x in liczby:
        print(f"sprawdzam {lic} : {x}")
        lic += 1
        ileroz = 0
        for i in range(1, x):
            if czy_pierwsza(i) and czy_pierwsza(x-i):
                ileroz += 1
        rozklady.append(ileroz)
        rozklady = sorted(rozklady)
        print(rozklady[len(rozklady)-1])
    #jak cos to to sie wykonuje nie wiadomo czemu jak tego nie usune
    #dobra to ogolnie bedzie dzialac ale wykonanie tego to zajmie godzine wiec polecam sprawdzic gdzie indziej rozwiazanie

def szesnastkowe():
    plik = open("/home/elliot/Downloads/Dane_2212/liczby.txt", "r")
    liczby_str = plik.readlines()
    liczby = []
    ile = 0
    for x in liczby_str:
        liczby.append(int(x))
    cyfry = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0,
    }
    for x in liczby:
        for x in range(x-1):
            while x > 0:
                reszta = x % 16
                if reszta < 10:
                    cyfry[reszta] += 1
                elif reszta == 11:
                    cyfry["A"] += 1
                elif reszta == 12:
                    cyfry["B"] += 1
                elif reszta == 13:
                    cyfry["C"] += 1
                elif reszta == 14:
                    cyfry["D"] += 1
                elif reszta == 15:
                    cyfry["E"] += 1
                elif reszta == 16:
                    cyfry["F"] += 1
                x = x // 16
    print(cyfry)



szesnastkowe()