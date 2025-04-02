def nieparzysty_skrot():
    #Nieparzysty skrót liczby całkowitej n nie istnieje, gdy jej zapis dziesiętny składa się tylko z cyfr parzystych
    ile = 0
    nieparzyste = []
    plik = open("/home/elliot/Downloads/Dane-NF-2405/skrot.txt", "r")
    linie = plik.readlines()
    liczby = []
    for x in linie:
        liczby.append(int(x))
    
    for x in linie:
        czy_nieparzysty = True
        for y in range(len(x)-1):
            liczba = int(x[y])
            if liczba / 2 != round(liczba / 2):
                czy_nieparzysty = False
            else:
                pass
        if czy_nieparzysty:
            ile += 1
            x = x[:-1]

            nieparzyste.append(int(x))
    print(ile)
    nieparzyste = sorted(nieparzyste)

    print(nieparzyste[len(nieparzyste)-1])


def NWD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def skroty():
    plik = open("/home/elliot/Downloads/Dane-NF-2405/skrot.txt", "r")
    linie = plik.readlines()
    liczby = []
    skroty = []

    for x in linie:
        x = x[:-2]
        liczby.append(x)
    
    for x in liczby:
        l = ""
        for y in range(len(x)):
            if int(x[y]) % 2 != 0:
                l = l + x[y]
        if len(l) > 0:
            skroty.append(l)
    print(skroty)




skroty()
