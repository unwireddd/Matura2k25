def bloki():
    liczby = open("/home/elliot/Downloads/Dane_2305/bin.txt")
    linie = liczby.readlines()
    wynik = 0
    for y in linie:
        ile = 1
        suma = 0
        blok = 0
        for x in range(0, len(y) - 1, 1):
            
            if y[x] == y[x + 1]:
                blok = 1
                suma += blok
            else:
                ile += 1
                #print(suma)
                pass
        #print(ile)
            if ile <= 2:
                wynik += 1
    print(ile)

def najwieksza():
        dziesietne = []
        
        liczby = open("/home/elliot/Downloads/Dane_2305/bin.txt")
        linie = liczby.readlines()
        linie_int = []
        for i in linie:
            linie_int.append(int(i))
        for x in linie:
            dziesietne.append(int(x, 2))
            #print(dziesietna)
        dziesietne.sort()
        dokonw = dziesietne[len(dziesietne) - 1]
        final = []
        while dokonw > 0:
            final.append(round(dokonw % 2))
            dokonw = dokonw // 2
        print(final)

                

                
najwieksza()