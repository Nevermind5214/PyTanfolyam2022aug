"""
Bizonyos karakterek
Írjunk egy függvényt a következő szignatúrával:
valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
A függvény egy olyan (akár üres) sztringgel térjen vissza, mely a "text"-ből (első paraméter) csak azokat a karaktereket tartalmazza, melyek szerepelnek a "chars"-ban.
Például:
valid("Barking!")                              -> "B"
valid("KL754", "0123456789")                   -> "754"
valid("BEAN", "abcdefghijklmnopqrstuvwxyz")    -> ""
"""

def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    return "".join([ch for ch in text if ch in chars])

def main():
    print(valid("Barking!"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))
    
if __name__ == "__main__":
    main()