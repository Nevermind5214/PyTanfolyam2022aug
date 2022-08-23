"""
XOR
A bool() beépített függvény eldönti a paraméterül kapott kifejezésről, hogy az igaz-e (True) vagy hamis (False).

Feladat

Adott két változó, s döntsük el, hogy teljesül-e az, hogy az egyik igazként míg a másik hamisként értékelődik ki. Ez tulajdonképpen egy XOR művelet (kizáró vagy), de most nem a bitműveletekre kell gondolni.

Példa:

str1 = "python"
str2 = None
Ekkor igaz az, hogy az egyik változó (str1) igazként, míg a másik (str2) hamisként lesz kiértékelve.

Tipp: merjük használni a bool() függvényt.
"""

def xor(a, b):
    return bool(a) != bool(b)

def main():
    str1 = "python"
    str2 = None
    print(xor(str1, str2))
    
if __name__ == "__main__":
    main()