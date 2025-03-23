def inna():
    plik = open("/home/elliot/Downloads/Dane_2212/mecz.txt", "r")
    linia = plik.readlines()
    licznik = 0
    linia = linia[0]
    print(linia)
    for x in range(1,len(linia)):
        #print(linia[x])
        #print(linia[x+1])
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


pierwszy_set()