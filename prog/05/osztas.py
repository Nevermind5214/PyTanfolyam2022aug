"""
Kivételek #2
Tekintsük az alábbi szkriptet.
A program bekér két számot, elosztja az elsőt a másodikkal,
majd kiírja az eredményt.

Feladat
Egészítsük ki a fenti programot úgy,
hogy kezeljük le a következő eseteket:
Ha a felhasználó nem számot adott meg,
akkor finoman tájékoztassuk a program helyes használatáról.

A programból CTRL+C-vel vagy CTRL+D-vel lehessen kilépni.
Ekkor a program ne produkáljon semmilyen hibaüzenetet.

Nullával való osztás esetén informatív hibaüzenet.
Haladjunk lépésenként.
Az egyes speciális eseteket egyenként, egymás után kezeljük le.
"""

def main():
    while True:
        try:
            szam1 = float(input("1. szam: "))
            szam2 = float(input("2. szam: "))
            result = szam1 / szam2
            print('Az osztas eredmenye: {0:.2f}'.format(result))
            print('-' * 10)
        except ValueError:
            print("Hiba: számot adj meg!")
        except ZeroDivisionError:
            print("Hiba: 0-val nem lehet osztani!")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()