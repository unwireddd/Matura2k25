
def czyPierwsza(liczba):
    if liczba < 2:
        return False
    x = 2
    while x < liczba:
        if liczba % x == 0:
            return False
        x += 1
    return True


def czyFibo(liczba):
    if liczba in tab_fibo:
        return True
    return False

def zad_14_1():
    ile = 0
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\14\liczby14.txt", "r")
    liczby = plik.readlines()
    for x in range(len(liczby)):
        liczby[x] = int(liczby[x])
    for x in liczby:
        if czyFibo(x):
           ile += 1

    return print(ile)

def zad_14_2():
    kat1 = []
    kat2 = []
    kat3 = []
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\14\liczby14.txt", "r")
    liczby_txt = plik.readlines()
    liczby = []
    for x in liczby_txt:
        liczby.append(int(x))
    for x in liczby:
        if czyFibo(x):
            continue
        else:
            for y in tab_fibo:
                if x == y + 1 or x == y -1:
                    kat1.append(x)
                if x == y + 2 or x == y -2:
                    kat2.append(x)
                if x == y + 3 or x == y -3:
                    kat3.append(x)
    kat1.sort()
    print(kat1)
    kat2.sort()
    print(kat2)
    kat3.sort()
    print(kat3)

def zad_14_3():
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\14\liczby14.txt", "r")
    liczby_txt = plik.readlines()
    liczby = []
    liczby2 = []
    for x in liczby_txt:
        liczby.append(int(x))
    for x in liczby:
        if czyFibo(x) and czyPierwsza(x):
            liczby2.append(x)
    liczby2.sort()
    print(liczby2)


#############################################################


tab_fibo = [0, 1]
while True:
    y = len(tab_fibo)
    if tab_fibo[y - 1] + tab_fibo[y - 2] >= 1000000000:
        break
    else:
        tab_fibo.append(tab_fibo[y - 1] + tab_fibo[y - 2])


#zad_14_1()
#zad_14_2()
zad_14_3()
