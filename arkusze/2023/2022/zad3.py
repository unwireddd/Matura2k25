def czy_pierwsza(liczba):
    ile = 0
    for x in range(1, liczba):
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
    
    for x in liczby:
        ileroz = 0
        for i in range(1, x):
            if czy_pierwsza(i) and czy_pierwsza(x-i):
                ileroz += 1
        rozklady.append(ileroz)
    ileroz = sorted(ileroz)
    print(ileroz(len(ileroz)-1))


goldbach()