# Test
def rozkladNaPierwsze(liczba):
    czynniki = []
    for i in range(2,liczba+1):
        while (liczba%i==0):
            czynniki.append(i)
            liczba //= i
        if liczba == 1:
            break
    return czynniki



def dzielniki():
    #dziala
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
    #podaj ile liczb z pierwszego wiersza jest dzielnikiem jakiejkolwiek liczby spośród liczb z drugiego wiersza
    for x in pierwsza:
        for y in druga:
            if y % x == 0:
                ile += 1
                break
    print(ile)

def stopierwsza():
    plik = open("/home/elliot/Downloads/Dane-NF-2405/liczby.txt", "r")
    linie = plik.readlines()
    pierwsza0 = linie[0].split(" ")
    pierwsza = []
    for x in pierwsza0:
        pierwsza.append(int(x))
    pierwsza = sorted(pierwsza)
    print(pierwsza[len(pierwsza)-102])

def iloczyn():
    #nie dziala
    liczby = []
    plik = open("/home/elliot/Downloads/Dane-NF-2405/liczby.txt", "r")
    linie = plik.readlines()
    pierwsza0 = linie[0].split(" ")
    pierwsza = []
    for x in pierwsza0:
        pierwsza.append(int(x))
    druga0 = linie[1].split(" ")
    druga = []
    for x in druga0:
        druga.append(int(x))
    
    for index in druga:
        for index2 in range(len(pierwsza)-1):
            for x in range(1, len(pierwsza)-1):
                if pierwsza[index2] * pierwsza[x] == index:
                    liczby += 1
    print(liczby)


def srednia(tab):
    suma = 0
    for x in tab:
        suma += x  
    return suma/len(tab)

def najwieksza_srednia():
    srednie = []
    plik = open("/home/elliot/Downloads/Dane-NF-2405/liczby.txt", "r")
    linie = plik.readlines()
    pierwsza0 = linie[0].split(" ")
    pierwsza = []
    for x in pierwsza0:
        pierwsza.append(int(x))
    
    for x in range(len(pierwsza)-50):
        print("sprawdzam")
        elementy = []
        for y in range(49):
            elementy.append(pierwsza[x + y])
            test = srednia(elementy)
            srednie.append(test)
        for z in range(pierwsza[x+49], len(pierwsza)-1):
            elementy.append(pierwsza[z])
            test = srednia(elementy)
            srednie.append(test)
    srednie = sorted(srednie)
    print(srednie[len(srednie)-1])

najwieksza_srednia()
        
