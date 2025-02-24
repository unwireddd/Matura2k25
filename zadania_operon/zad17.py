def zad_17_1():
    kobiety = 0
    mezczyzni = 0
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\17\pesel.txt", "r")
    pesele = plik.readlines()

    for x in pesele:
        if int(x[9]) % 2 == 0:
            kobiety += 1
        else:
            mezczyzni += 1
    print(mezczyzni)
    print(kobiety)

def algorytm(pesel):
    suma = 0
    suma += (int(pesel[0]) * 1) %10
    suma += (int(pesel[1]) * 3) %10
    suma += (int(pesel[2]) * 7) %10
    suma += (int(pesel[3]) * 9) %10
    suma += (int(pesel[4]) * 1) %10
    suma += (int(pesel[5]) * 3) %10
    suma += (int(pesel[6]) * 7) %10
    suma += (int(pesel[7]) * 9) %10
    suma += (int(pesel[8]) * 1) %10
    suma += (int(pesel[9]) * 3) %10
    suma = suma % 10
    wynik = 10-suma
    if int(pesel[10]) != wynik:
        return False
    return True

def zad_17_2():
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\17\pesel.txt", "r")
    pesele = plik.readlines()
    for x in pesele:
        if not algorytm(x):
            print(x)

#zad_17_2()
def rok_urodzenia(pesel):
    miesiac = int(pesel[2:4])
    rok = int(pesel[0:2])
    if miesiac > 80:
        baza = 1800
    elif miesiac > 20:
        baza = 2000
    else:
        baza = 1900
    return baza + rok

def zad_17_3():
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\17\pesel.txt", "r")
    pesele = plik.readlines()
    tab = [0] *4
    for x in pesele:
        if 2022 - rok_urodzenia(x) <= 18:
            tab[0] += 1
        elif 2022 - rok_urodzenia(x) <= 50:
            tab[1] += 1
        elif 2022 - rok_urodzenia(x) <= 100:
            tab[2] += 1
        else:
            tab[3] += 1
    print(tab)

zad_17_3()






