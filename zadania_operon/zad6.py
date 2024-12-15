

def ciag(n):
    l1 = 0
    l2 = 1
    liczby = [1, 1]

    if n == 1:
        return "TAK"

    while True:
        liczby.append(liczby[l1] + liczby[l2])
        if liczby[len(liczby) - 1] == n:
            return "TAK"
        if liczby[len(liczby) - 1] > n:
            return "NIE"
        l1 += 1
        l2 += 1

def szyfruj(n, tekst):
    l1 = 0
    l2 = 1
    liczby = [1, 1]

    for x in range(len(tekst) - 2):
        liczby.append((liczby[l1] + liczby[l2]) % n)

        l1 += 1
        l2 += 1
    print(liczby)

    tab2 = []
    for x in range(len(liczby)):
        c = ord(tekst[x]) + liczby[x]
        if c > ord('Z'):
            c = c - (ord('Z') - ord('A') + 1)
        tab2.append(chr(c))
    print("".join(tab2))
    test = ""
    for x in range(len(tab2)):
        test = test + tab2[x]

    print(test)

szyfruj(20, "DOSTAWAWCZWARTEK")