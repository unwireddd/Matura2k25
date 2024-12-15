import math

def czy_pierwsza(n):
    pierw = int(math.sqrt(n))
    x = 2
    while x <= pierw:
        if (n % x) == 0:
            return False
        else:
            x = x + 1
    return True

def wypisywanie():
    n = 1

    for n in range(1, 100001, 1):
        if czy_pierwsza(n):
            pom = n
            #print(n)
            suma = 0
            while pom > 0:
                suma = suma + pom%10
                pom = pom // 10
            if czy_pierwsza(suma):
                pom = n
                # print(n)
                suma = 0
                while pom > 0:
                    suma = suma + pom % 2
                    pom = pom // 2
                if czy_pierwsza(suma):
                    print(n)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # if czy_pierwsza(4):
    #     print("Liczba jest pierwsza")
    # else:
    #     print("Liczba nie jest pierwsza")
    wypisywanie()