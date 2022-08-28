"""
Hamming-távolság

A Hamming-távolság alatt két azonos hosszúságú karaktersorozat eltérő karaktereinek a számát értjük.

Példa:
tOnEd
rOsEs
A szavak a vastagon jelzett pozíciókban eltérnek, így a két szó Hamming-távolsága: 3.

Írjon egy függvényt, mely megállapítja a paraméterül kapott sztringek Hamming-távolságát.

Speciális eset

Gondolkodjon el azon, hogy hogyan kezelné le azt az esetet, amikor a két sztring hossza különbözik.

Segítség: a sztringeket tilos módosítani! Ha a két sztring hossza eltér, akkor a sztringekre nem értelmezett a Hamming-távolság. Ezt hogyan tudnánk jelezni a hívó félnek?
"""
import sys

def hamming(w1,w2):
    if len(w1) != len(w2):
        print("A két szó egyenlő hosszú kell legyen!")
        sys.exit(1)
        #return -1
    cnt = 0
    for ch1, ch2 in zip(w1,w2):
        if ch1 != ch2: cnt += 1
    return cnt

def main():
    print(hamming("toned","roses"))
    
if __name__ == "__main__":
    main()