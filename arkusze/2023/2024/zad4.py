def najwieksze_pola():
    #dziala
        liczby = open("/home/elliot/Downloads/Dane-2412/prostokaty.txt")
        linie = liczby.readlines()
        wyniki = []
        min = 0
        max = 0
        for x in linie:
            a = int(x.split()[0])
            b = int(x.split()[1])
            wynik = a * b
            wyniki.append(wynik)
        wyniki = sorted(wyniki)
        print(wyniki[0])
        print(wyniki[len(wyniki) - 1])
def czy_miesci():
    #nie dziala
        liczby = open("/home/elliot/Downloads/Dane-2412/prostokaty.txt")
        linie = liczby.readlines()
        wyniki = []
        dlugosc = 0
        dlugosci = []
        for x in linie:
            a = int(x.split()[0])
            b = int(x.split()[1])
            wynik = a * b
            wyniki.append(wynik)
        for x in range(len(wyniki)-1):
            if wyniki[x] == wyniki[x+1]:
                dlugosc += 1
            else:
                dlugosci.append(dlugosc)
                dlugosc = 0
        final = sorted(dlugosci)
        print(final)
            


czy_miesci()