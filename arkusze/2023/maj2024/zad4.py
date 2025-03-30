def dzielniki():
    #nie dziala
    ile = 0
    plik = open("/home/elliot/Downloads/Dane-NF-2405/liczby.txt", "r")
    linie = plik.readlines()
    pierwsza0 = linie[0].split()
    druga0 = linie[1].split()
    pierwsza = []
    druga = []
    for x in pierwsza0:
        pierwsza.append(int(x))
    for x in druga0:
        druga.append(int(x))
    for x in druga:
        for y in pierwsza:
            if x % y == 0:
                ile += 1
                
    print(ile)

dzielniki()