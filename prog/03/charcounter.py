"""
Karakterszámláló
Írjunk egy charcount(text) szignatúrájú függvényt. 
A függvény paraméterként kapjon egy angol szöveget, visszatérési értéke pedig egy 28 elemű szótár legyen.
A szótár kulcsai a következők legyenek: az angol ábécé kisbetűi ("a", "b", …, "z"), "whitespace", illetve "other".
A szótár kulcsaihoz rendelt értékek azt mutassák, hogy az adott karakter hányszor fordul elő a paraméterként átadott sztringben.
Például:
charcount("cat and dog")
visszatérési értéke:
{'whitespace': 2, 'others': 0, 'a': 2, 'b': 0, 'c': 1, ..., 't': 1, ..., 'z': 0}
"""

import string

def charcount(text):
    cdict = {}
    cdict["whitespace"] = 0
    cdict["others"] = 0
    for chr in string.ascii_lowercase:
        cdict[chr] = 0

    for char in text:
        if char in string.ascii_lowercase:
            cdict[char] += 1
        elif char.isspace(): cdict["whitespace"] += 1
        else: cdict["others"] += 1
    return cdict

def main():
    print(charcount("cat and dog"))
    
if __name__ == "__main__":
    main()