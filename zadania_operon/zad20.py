def anagram(wyraz1, wyraz2):
    w1 = list(wyraz1)
    w2 = list(wyraz2)
    if len(w1) != len(w2):
        return False
    w1.sort()
    w2.sort()
    if w1 == w2:
        return True

    return False

def anagram2(wyraz1, wyraz2):
    alfabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
               "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    w1 = list(wyraz1)
    w2 = list(wyraz2)
    if len(w1) != len(w2):
        return False
    for x in range(len(w1)):
        c = w2[x]
        for i in alfabet:
            w2[x] = i
            if anagram("".join(w1), "".join(w2)):
                print("".join(w1))
                print("".join(w2))
                print(x + 1)
                print(i)
                return
        w2[x] = c


def zad_20_1():
    ile = 0
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\20\anagramy.txt", "r")
    pary = plik.readlines()
    for para in pary:
        wyrazy = para.split()
        if anagram(wyrazy[0], wyrazy[1]):
            ile += 1
    print(ile)

def zad_20_2():

    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\20\anagramy.txt", "r")
    pary = plik.readlines()
    for para in pary:
        wyrazy = para.split()
        if not anagram(wyrazy[0], wyrazy[1]):
            anagram2(wyrazy[0], wyrazy[1])

def anagramy(w):
    lista = []
    if len(w) <= 1:
        return [w]
    for i in range(len(w)):
        c = w[i]
        a = anagramy(w[:i] + w[i + 1:])
        for x in a:
            lista.append(c + x)
    return list(set(lista))

def zad_20_4():
    plik = open(r"C:\Kuba\informatyka\informatyka-repetytorium\rozdział 2\pliki\20\wyrazy.txt", "r")
    wyrazy = plik.readlines()
    for x in wyrazy:
        print(anagramy(x))


zad_20_4()
