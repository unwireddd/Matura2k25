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
    #dalej nie dziala
        liczby = open("/home/elliot/Downloads/Dane-2412/prostokaty_przyklad.txt")
        linie = liczby.readlines()
        wyniki = []
        dlugosc = 0
        dlugosci = []
        for x in range(1,len(linie)):
            a = int(linie[x].split()[0])
            b = int(linie[x].split()[1])
            print("")
            print(a)
            print(b)
            
            print(int(linie[x-1].split()[0]))
            print(int(linie[x-1].split()[1]))
            print("")
            if a <= int(linie[x-1].split()[0]) and b <= int(linie[x-1].split()[1]):
                dlugosc += 1
            else:
                dlugosci.append(dlugosc)
                dlugosc = 0
        print(dlugosci)
        dlugosci = sorted(dlugosci)
        print(dlugosci[len(dlugosci)-1])


        


czy_miesci()