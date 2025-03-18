def dwucyfrowe():
    plik = open("/home/elliot/Downloads/Dane_2305/pi.txt", "r")
    linie = plik.readlines()
    liczby = []
    liczby2 = []

    for x in range(len(linie)-1):
        wynik = f"{linie[x]}{linie[x + 1]}"
        wynik = wynik.replace("\n", "")
        liczby.append(wynik)
    print(liczby)
    for x in liczby:
        liczby2.append(int(x))
    licznik = 0
    for x in liczby2:
        if x > 90:
            licznik += 1
    
    print(licznik)

def naj():
    plik = open("/home/elliot/Downloads/Dane_2305/pi.txt", "r")
    linie = plik.readlines()
    liczby1 = []
    liczby = {
        "00": 0,
        "01": 0,
        "02": 0,
        "03": 0,
        "04": 0,
        "05": 0,
        "06": 0,
        "07": 0,
        "08": 0,
        "09": 0,

    }
    for x in range(10, 100, 1):
        liczby[str(x)] = 0
    #print(liczby)

    for x in range(len(linie)-1):
        wynik = f"{linie[x]}{linie[x + 1]}"
        wynik = wynik.replace("\n", "")
        liczby1.append(wynik)


    for x in liczby1:
        liczby[x] += 1

    print(sorted(liczby, key=liczby.get))


def rosnocamalejace():
        plik = open("/home/elliot/Downloads/Dane_2305/pi.txt", "r")
        linie = plik.readlines()
        tab = []
        tab1 = []
        for x in range(len(linie) - 5):
            i = 0
            ciag = []
            while i < 6:
                ciag.append(int(linie[x + i]))
                i += 1
            tab.append(ciag)
        print(tab)

        licznik = 0
        for x in tab:
            if x[0] < x[1] < x[2] and x[3] > x[4] > x[5]:
                licznik += 1
            elif x[0] < x[1] < x[2] < x[3] and x[4] > x[5]:
                licznik += 1
            elif x[0] < x[1] and x[2] > x[3] > x[4] > x[5]:
                licznik += 1
            else:
                pass


        print(licznik)

def czyrosmal(x):
    for i in range(len(x)):
        

def najdluzszy():
        plik = open("/home/elliot/Downloads/Dane_2305/pi.txt", "r")
        linie = plik.readlines()
        pi = []
        for x in linie:
            pi.append(int(x))
        max = []
        for index in range(len(pi)):
            tab = [pi[index]]
            x = 1
            while x < len(pi) - index:
                tab.append(pi[index + x])
                if czyrosmal(tab) and len(tab) > len(max):
                    max = tab

najdluzszy()
                
                






#dwucyfrowe()

