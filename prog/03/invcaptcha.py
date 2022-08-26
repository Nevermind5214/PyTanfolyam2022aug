"""
AoC2017, Day 1, Part 1 (Inverse Captcha)

A bemenet egy számsorozat. Állapítsuk meg azon számjegyek összegét, amelyek azonosak a rákövetkező számjeggyel.
A számsorozat cirkuláris, vagyis az utolsó számjegy rákövetkezője a legelső számjegy.

Példa:

1122 esetén az összeg 3 (1 + 2) ui. az első számjegy (1) megegyezik a másodikkal és a harmadik számjegy (2) megegyezik a negyedikkel
1111 esetén az eredmény 4 mivel minden számjegy (az összes 1-es) egyezik a rákövetkezőjével
1234 esetén a kimenet 0 mivel egyetlen számjegy sem egyezik a rákövetkezőjével
91212129 esetén az eredmény 9 mivel csak a legutolsó számjegy (a 9-es) egyezik a rákövetkezőjével

Próbáljuk meg használni a zip() függvényt. List comprehension-t be tudunk csempészni?
"""
def rakovtest(szam):
    osszeg = 0
    for i in range(0,len(str(szam))-1):
        if str(szam)[i] == str(szam)[i+1]: osszeg += int(str(szam)[i])
    if str(szam)[-1] == str(szam)[0]: osszeg += int(str(szam)[-1])  
    return osszeg

def main():
    with open("day01.txt", "r") as file:
        szam=file.readline()
    print(rakovtest(1122))
    print(rakovtest(1111))
    print(rakovtest(1234))
    print(rakovtest(91212129))
    print(rakovtest(szam))
    
if __name__ == "__main__":
    main()