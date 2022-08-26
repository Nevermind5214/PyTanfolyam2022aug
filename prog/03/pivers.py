"""
PI vers

A PI értékét a következőképpen is le tudjuk kérdezni:

import math

print(math.pi)    # 3.141592653589793
Most tekintsük az alábbi verset:

How I want a drink
alcoholic of course
After the heavy lectures
involving complex functions
Ha vesszük az egyes szavak hosszát, akkor a PI első 15 számjegyét kapjuk eredményül. Írjunk egy kis programot amivel ezt le tudjuk ellenőrizni.

Haladóbbaknak: oldjuk meg a problémát list comprehension használatával.
"""
import math

TEXT = "How I want a drink alcoholic of course After the heavy lectures involving complex functions"

def textwordcharcount(text):
    return [len(n) for n in text.split()]

def getpidigits(num):
    return str(int(math.pi*10**(num-1)))[:num]

def main():
    print("Szöveg karakterszámai:\n","".join([str(n) for n in textwordcharcount(TEXT)]))
    print("PI jegyei:\n",getpidigits(len("".join([str(n) for n in textwordcharcount(TEXT)]))))

if __name__ == "__main__":
    main()