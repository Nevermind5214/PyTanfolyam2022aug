"""
A 8 királynő probléma a következőképpen hangzik:
egy sakktáblán helyezzünk el 8 királynőt úgy, hogy ne üssék egymást.

A feladat most csak annyi lesz, hogy egy lehetséges állást jelenítsünk meg "grafikusan".
A sakktáblát mátrix helyett egy tömbben (listában) reprezentáljuk, pl.: [7,3,0,2,5,1,6,4].
Ennek jelentése: az 1. oszlopban a királynő alulról a 8. sorban van, a 2. oszlopban alulról a 4. sorban, stb.
(A listában a sorok indexelése 0-tól indul.) Ebből a listából a következő sakktáblát lehetne megjeleníteni:
+-----------------+
| Q . . . . . . . |
| . . . . . . Q . |
| . . . . Q . . . |
| . . . . . . . Q |
| . Q . . . . . . |
| . . . Q . . . . |
| . . . . . Q . . |
| . . Q . . . . . |
+-----------------+
Feladat: írjunk egy olyan eljárást, mely kap egy 8 elemű listát, s ez alapján megrajzolja a sakktáblát.
Például ha a bemenet [0,4,7,5,2,6,1,3], akkor egy ilyen sakktáblát kellene kirajzolni:
+-----------------+
| . . Q . . . . . |
| . . . . . Q . . |
| . . . Q . . . . |
| . Q . . . . . . |
| . . . . . . . Q |
| . . . . Q . . . |
| . . . . . . Q . |
| Q . . . . . . . |
+-----------------+
Mire figyeljünk:

A kirajzolt sakktábla négyzet alakú legyen.
Rajzoljuk meg a keretet is.
"""
def sakk(tabla):
    print("+-----------------+")
    for i in range(0,8):
        print("|",end="")
        for queen in tabla:
            if queen == i: print(" Q", end="")
            else: print(" .", end="")
        print(" |")
    print("+-----------------+")

def main():
    sakk([7,3,0,2,5,1,6,4])
    print()
    sakk([0,4,7,5,2,6,1,3])
    
if __name__ == "__main__":
    main()