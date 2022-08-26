"""
100 db 50-jegyű szám (PE #13)
Határozzuk meg a köv. 100 db 50-jegyű szám összegének az első tíz számjegyét.
Tipp: a fenti adattömeget nehogy egy függvényen belülre tegyük!
A számokat mentsük le egy file-ba s úgy dolgozzuk fel őket.
"""

def main():
    mysumma = 0
    with open("100db50jegyu.txt", "r") as file:
        for line in file:
            mysumma += int(line)

    print(mysumma)
    print(str(mysumma)[:10])
    
if __name__ == "__main__":
    main()