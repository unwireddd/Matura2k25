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

def zad_18_1():
    s = [0] * 17

    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\18\trzyliczby.txt", "r")
    liczby = plik.readlines()
    for x in liczby:
        trzy = x.split()
        for system in range(2,17):
            zero = konwert(trzy[0], system)
            jeden = konwert(trzy[1], system)
            dwa = konwert(trzy[2], system)
            if zero + jeden == dwa:
                s[system] += 1
                break
    print(s[2:17])

zad_18_1()






