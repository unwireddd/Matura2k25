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

nieparzysty_skrot()
