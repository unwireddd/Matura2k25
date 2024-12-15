
def fun(n):
    k = 0
    p = 2
    while n > 1:
        if (n % p) == 0:
            k += 1
            while (n % p) == 0 and n > 1:
                n = n // p
        p += 1
    if (k % 2) == 0:
        print("TAK")
    else:
        print("NIE")


def fun_kuba(n):
    k = 0
    p = 2
    tab = {}
    while n > 1:
        if (n % p) == 0:
            k += 1
            tab[p] = 0
            while (n % p) == 0 and n > 1:
                n = n // p
                tab[p] += 1
        p += 1
   # print(tab)

    pom_p = 0
    pom_k = 0
    pom_k2 = 0
    for x in tab:
        if tab[x] > pom_k:
            pom_k = tab[x]
            pom_p = x
    for x in tab:
        if x != pom_p:
            if tab[x] == pom_k:
                print("BRAK")
                return
    print(f"{pom_p} {pom_k}")















def fun_mod(n):
    k = 0
    p = 2
    podzielniki = {}
    while n > 1:
        if (n % p) == 0:
            k += 1
            podzielniki[p] = 0
            while (n % p) == 0 and n > 1:
                n = n // p
                podzielniki[p] += 1
        p += 1

    dom_n = 0
    dom_pod = 1
    for pod in podzielniki:
        if podzielniki[pod] == dom_n:
            print("BRAK")
            return
        if podzielniki[pod] > dom_n:
            dom_pod = pod
            dom_n = podzielniki[pod]
    print(f"{dom_pod} {dom_n}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # fun(55)
    # fun(64)
    # fun(92)
    # fun(210)
    # fun(215)

    # fun_mod(64)
    # fun_mod(54)
    # fun_mod(15)

    fun_kuba(64)
    fun_kuba(54)
    fun_kuba(15)
