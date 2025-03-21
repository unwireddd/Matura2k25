def czy_pierwsza(liczba):
    dzielniki = 0
    for x in range(1, liczba // 2, 1):
        if liczba % x == 0:
            dzielniki += 1
    if dzielniki == 1:
        return True
    return False



#do drugiego bo generalnie w analizie kodu latwiej jest po prostu przepisac go do pythona
def F(x,p):
    print("a")
    if x == 0:
        return 0
    else:
        c = x % p
        if c % 2 == 1:
            return F(x // p,p) + c
        else:
            return F(x // p,p) - c

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

def dzielniki_pierwsze():
        plik = open("/home/elliot/Downloads/Dane-2412/liczby.txt", "r")
        lin = plik.readlines()
        linie = []
        for x in lin:
            linie.append(int(x))
        for x in linie:
            dzielniki = 0
            for i in range(x):
                if czy_pierwsza(i) and x % i == 0:
                    dzielniki += 1
            if dzielniki >= 5:
                print(x)


#kwadraty()
def najwieksza_najmniejsza():
        plik = open("/home/elliot/Downloads/Dane-2412/liczby.txt", "r")
        lin = plik.readlines()
        linie = []
        ile_mniejszych = 0
        ile_wiekszych = 0
        ile_rownych = 0
        for x in lin:
            linie.append(int(x))
        for x in lin:
            najwieksza = 0
            najmniejsza = 0
            tab = []
            for i in range(len(x)):
                tab.append(x[i])
            sort1 = tab.sort()
            sort = []
            for x in sort1:
                sort.append(str(x))
            sort2 = []
            for x in range(len(sort1), 0, -1):
                sort2.append(str(x))
            najwieksza = sort[0] + sort[1] + sort[2] + sort[3]
            najmniejsza = sort2[0] + sort2[1] + sort2[2] + sort2[3]
            najwieksza = int(najwieksza)
            namniejsza = int(najmniejsza)
            final = najwieksza - najmniejsza
            if x > final:
                ile_mniejszych += 1
            elif x < final:
                ile_wiekszych += 1
            elif x == final:
                ile_rownych += 1
            print(ile_mniejszych)
            print(ile_wiekszych)
            print(ile_rownych)

            #jeszcze nie dziala


            
najwieksza_najmniejsza()
