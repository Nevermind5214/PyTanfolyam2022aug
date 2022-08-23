"""
Ezernél kisebb pozitív egész számok (PE #1)

Ha felsoroljuk a 10-nél kisebb pozitív egész számokat, melyek 3-nak vagy 5-nek a többszörösei, akkor a köv. számokat kapjuk: 3, 5, 6 és 9. Ezek összege 23.

Állapítsuk meg azon 1000-nél kisebb számok összegét, melyek 3-nak vagy 5-nek a többszörösei.

Haladó

Oldjuk meg a problémát egy (azaz 1) sorban list comprehension segítségével. Tipp: használjuk a sum beépített függvényt.
"""


def main():
    print(sum([n for n in range(0,10) if n % 3 == 0 or n % 5 == 0]))
    print(sum([n for n in range(0,1000) if n % 3 == 0 or n % 5 == 0]))
    
if __name__ == "__main__":
    main()