"""
Az alábbi kódrészlet 100 db random számjegyet állít elő s nyomtat ki egymás mellé:

import sys
import random as r

UPTO = 100


def main():
    for i in range(UPTO):
        print(r.randint(0, 9), end="")
    print()
Módosítsuk a kódot úgy, hogy egy sorba csak 10 számjegy kerüljön. Példa:

8816362140
4460651954
6917509824
6810211402
3696392147
9637243638
4462786058
2306285239
0826916343
1837115597
"""

import sys
import random as r

UPTO = 100


def main():
    for i in range(0,UPTO):
        print(r.randint(0, 9), end="")
        if (i + 1) % 10 == 0: print()
    print()

if __name__ == "__main__":
    main()