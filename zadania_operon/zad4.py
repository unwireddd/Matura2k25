# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def oblicz(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if (n % 2) == 0:
        return pow(oblicz(x, n / 2), 2)
    else:
        return x * pow(oblicz(x, (n - 1) / 2), 2)










def oblicznew(x, n):
    reszty = []
    w = x

    while n > 1:
        reszty.append(n % 2)
        n //= 2

    while len(reszty) > 0:
        w *= w
        if reszty.pop() > 0:
            w *= x

    return w

def obliczi(x, n):
    w = 1
    while n > 0:
        if (n % 2) == 1:
            w *= x
        x *= x
        n //= 2
    return w

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #if False:
        print(f"2^10 : {oblicz(2, 10)}")
        print(f"7^13 : {oblicz(7, 13)}")
        print(f"4^16 : {oblicz(4, 16)}")
        print(f"3^35 : {oblicz(3, 35)}")
    #else:
        print(f"2^10 : {oblicznew(2, 10)}")
        print(f"7^13 : {oblicznew(7, 13)}")
        print(f"4^16 : {oblicznew(4, 16)}")
        print(f"3^35 : {oblicznew(3, 35)}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
