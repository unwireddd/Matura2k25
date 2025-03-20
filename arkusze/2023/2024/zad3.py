def pierwiastek(liczba):
    for x in range(liczba // 2):
        if x * x == liczba:
            return x

def kwadraty():
    plik = open("/home/elliot/Downloads/Dane-2412/liczby.txt", "r")
    lin = plik.readlines()
    linie = []
    pierwsza = 0
    licz = 0
    for x in lin:
        linie.append(int(x))
    #pierwsza
    for x in linie:
        if pierwiastek(x):
            pierwsza = x
            break
    for x in linie:
        if pierwiastek(x):
            licz += 1
    print(pierwsza)
    print(licz)


kwadraty()