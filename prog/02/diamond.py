#!/usr/bin/env python3

"""
Írjunk egy függvényt, mely paraméterként megkapja egy gyémánt magasságát. A függvény ezek után rajzolja ki a gyémántot a következőképpen:

Magasság: 3

 *
***
 *
Magasság: 7

   *
  ***
 *****
*******
 *****
  ***
   *
Csak páratlan magasságot fogadjunk el! Páros érték esetén írjunk ki egy informatív hibaüzenetet!

Tipp: nézzük meg a center() nevű sztringmetódust… (← Python esetén)
string.center(length, character)
The center() method will center align the string, using a specified character (space is default) as the fill character.

txt = "banana"

x = txt.center(20, "O")
OOOOOOObananaOOOOOOO
"""

def dia(m):
    if m % 2 == 1:
        for n in range(1, int(m/2)+1):
            print(("*"*(n*2-1)).center(m))
        for n in range(int(m/2)+1, 0, -1):
            print(("*"*(n*2-1)).center(m))
    else: print("Csak a páratlan magasság elfogadott!")

def main():
    dia(int(input("Magasság: ")))
    
if __name__ == "__main__":
    main()