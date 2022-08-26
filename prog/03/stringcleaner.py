"""
A string1.py file-ból távolítsuk el a megjegyzéseket. Az egyszerűség kedvéért csak azokat a sorokat töröljük, amelyek # jellel kezdődnek.
A kimenetet egy string1_clean.py nevű file-ba írjuk ki.
Távolítsuk el azokat a megjegyzéseket is, ahol a # jel indentálva szerepel, pl.:
"""

def main():
    print("HI!")
    count = 0
    written = 0
    with open("string1.py", "r") as filein, open ("string1_clean.py", "w") as fileout:
        for line in filein:
            count += 1
            if not line.strip().startswith("#") and line.strip() != "":
                fileout.write(line)
                written += 1
    print(f"{count} lines read.")
    print(f"{written} lines written.")
    print(f"{count - written} comment lines removed.")

if __name__ == "__main__":
    main()