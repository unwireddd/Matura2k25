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


#dwucyfrowe()
naj()
