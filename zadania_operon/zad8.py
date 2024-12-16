
def convert_r2d(roman):
    rzymskie = {
        "I":    1,
        "V":    5,
        "X":    10,
        "L":    50,
        "C":    100,
        "D":    500,
        "M":    1000,
    }
    liczba = 0
    poprzednia = 0
    for x in reversed(range(len(roman))):
        if rzymskie[roman[x]] >= poprzednia:
            liczba += rzymskie[roman[x]]
        else:
            liczba -= rzymskie[roman[x]]
        poprzednia = rzymskie[roman[x]]

    print(liczba)


def convert_d2r(decimal):
    rzymskie = { 1: 'I',
                2: 'II',
                3: 'III',
                4: 'IV',
                5: 'V',
                6: 'VI',
                7: 'VII',
                8: 'VIII',
                9: 'IX',
                10: 'X',
                20: 'XX',
                30: 'XXX',
                40: 'XL',
                50: 'L',
                60: 'LX',
                70: 'LXX',
                80: 'LXXX',
                90: 'XC',
                100: 'C',
                200: 'CC',
                300: 'CCC',
                400: 'CD',
                500: 'D',
                600: 'DC',
                700: 'DCC',
                800: 'DCCC',
                900: 'CM',
                1000: 'M',
                2000: 'MM',
                3000: 'MMM',
                }
    wynik = ''
    dzielnik = 1
    while decimal > 0:
        cyfra = decimal % 10
        if cyfra > 0:
            wynik = rzymskie[(cyfra * dzielnik)] + wynik
        decimal = decimal // 10
        dzielnik *= 10
    print(wynik)

# convert_r2d("I")
# convert_r2d("III")
# convert_r2d("IV")
# convert_r2d("VII")
# convert_r2d("IX")
# convert_r2d("XVI")
# convert_r2d("LXIX")
# convert_r2d("CDLXXXI")
# convert_r2d("MMXXIV")

convert_d2r(1)
convert_d2r(3)
convert_d2r(4)
convert_d2r(7)
convert_d2r(9)
convert_d2r(16)
convert_d2r(69)
convert_d2r(481)
convert_d2r(2024)
