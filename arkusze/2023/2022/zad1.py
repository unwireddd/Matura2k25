def inna():
    plik = open("/home/elliot/Downloads/Dane_2212/mecz.txt", "r")
    linia = plik.readlines()
    licznik = 0
    linia = linia[0]
    print(linia)
    for x in range(1,len(linia)):
        if linia[x] != linia[x-1]:
            licznik += 1
    print(licznik)

def pierwszy_set():
    plik = open("/home/elliot/Downloads/Dane_2212/mecz.txt", "r")
    linia = plik.readlines()
    licznik = 0
    linia = linia[0]
    a = 0
    b = 0
    for x in range(len(linia)):
        if linia[x] == "A":
            a += 1
        else:
            b += 1
        if a >= 1000 or b >= 1000:
            if a+3 <= b or b+3 <= a:
                print(a)
                print(b)
                break

def dobra_passa():
    plik = open("/home/elliot/Downloads/Dane_2212/mecz.txt", "r")
    linia = plik.readlines()
    linia = linia[0]
    passy = []
    licznik = 0
    ile = 0
    for x in range(len(linia)-1):
        if linia[x] == linia[x+1]:
            licznik += 1
        else:
            licznik += 1
            if licznik >= 10:
                ile += 1
                passy.append(licznik)
                licznik = 0
            licznik = 0
    print(ile)
    passy = sorted(passy)
    indeks = passy[len(passy)-1]
    print(passy[len(passy)-1])

    for x in range(len(linia)-1):
        if linia[x] == linia[x+1]:
            licznik += 1
        else:
            licznik += 1
            if licznik == indeks:
                print(linia[x])
            licznik = 0



dobra_passa()