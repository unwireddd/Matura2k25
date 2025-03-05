def konwert(liczba, system):

    ascii = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }
    x = len(liczba)
    m = 1
    suma = 0
    while x > 0:
        x -= 1
        suma += ascii[liczba[x]] * m
        m *= system

    return suma

print(konwert("FF", 16))

systemy = []

def zad_18_1():
    s = [0] * 17

    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\18\trzyliczby.txt", "r")
    liczby = plik.readlines()
    for x in liczby:
        if "A" in x or "B" in x or "C" in x or "D" in x or "E" in x or "F" in x:
            systemstart = 11
        else:
            systemstart = 2
        trzy = x.split()
        for system in range(systemstart,17):
            zero = konwert(trzy[0], system)
            jeden = konwert(trzy[1], system)
            dwa = konwert(trzy[2], system)
            if zero + jeden == dwa:
                systemy.append(system)
                s[system] += 1
                break
    print(s[2:17])

def zad_18_2():
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\18\trzyliczby.txt", "r")
    liczby = plik.readlines()
    y = 0
    min = 99999999999999999999999
    max = 0
    for x in liczby:
        trzy = x.split()
        n = konwert(trzy[0], systemy[y])
        if n > max:
            max = n
        if n < min:
            min = n
        n = konwert(trzy[1], systemy[y])
        if n > max:
            max = n
        if n < min:
            min = n
        n = konwert(trzy[2], systemy[y])
        if n > max:
            max = n
        if n < min:
            min = n
        y += 1
    print(min)
    print(max)

def zad_18_3():
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\18\trzyliczby.txt", "r")
    liczby = plik.readlines()
    tab = {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0,

    }
    for x in liczby:
        trzy = x.split()
        for c in trzy[0]:
            tab[c] += 1
        for c in trzy[1]:
            tab[c] += 1
        for c in trzy[2]:
            tab[c] += 1
    print(tab)

    suma = 0
    for c in tab:
        suma += tab[c]

    for c in tab:
        print(f"{c}: {(tab[c] / suma)*100.0:.2f}")




zad_18_3()









