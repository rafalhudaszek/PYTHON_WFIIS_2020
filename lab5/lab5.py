
def task1(liczba):
    roman = ""
    if liczba >= 4000:
        print("liczba jest zbyt duża")
    else:
        while liczba > 0:
            if liczba >= 1000:
                roman = roman + "M"
                liczba = liczba - 1000
            elif liczba >= 900:
                roman = roman + "CM"
                liczba = liczba - 900
            elif liczba >=500:
                roman = roman + "D"
                liczba = liczba - 500
            elif liczba >=400:
                roman = roman + "CD"
                liczba = liczba - 400
            elif liczba >=100:
                roman = roman + "C"
                liczba = liczba - 100
            elif liczba >=90:
                roman = roman + "XC"
                liczba = liczba - 90
            elif liczba >=50:
                roman = roman + "L"
                liczba = liczba - 50
            elif liczba >=40:
                roman = roman + "XL"
                liczba = liczba - 40
            elif liczba >=10:
                roman = roman + "X"
                liczba = liczba - 10
            elif liczba >=9:
                roman = roman + "IX"
                liczba = liczba - 9
            elif liczba >=5:
                roman = roman + "V"
                liczba = liczba - 5
            elif liczba >=4:
                roman = roman + "IV"
                liczba = liczba - 4
            elif liczba >=1:
                roman = roman + "I"
                liczba = liczba - 1
        return roman
print(task1(1923))


def task2(roman):
    iterator = 0
    arabic = 0
    s = {}
    s["I"] = 1
    s["IV"] = 4
    s["V"] = 5
    s["IX"] = 9
    s["X"] = 10
    s["XL"] = 40
    s["L"] = 50
    s["XC"] = 90
    s["C"] = 100
    s["CD"] = 400
    s["D"] = 500
    s["CM"] = 900
    s["M"] = 1000
    while iterator < len(roman) - 1:
        if (roman[iterator] + roman[iterator + 1]) in s:
            arabic = arabic + s[str(roman[iterator] + roman[iterator + 1])]
            iterator = iterator + 2
        else:
            arabic = arabic + s[str(roman[iterator])]
            iterator = iterator + 1
    arabic = arabic + s[str(roman[iterator])]
    print(arabic) 
