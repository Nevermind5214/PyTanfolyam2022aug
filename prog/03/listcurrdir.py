#ls, először könyvtárak, utána fájlok és abc sorrend
import os

def main():
    entries = {}
    for elem in os.listdir("."):
        if os.path.isdir(elem):
            entries[elem] = "dir"
        elif os.path.isfile(elem):
            entries[elem] = "file"
        else: entries[elem] = "idkwtf"

    for dir in sorted(entries):
        if entries[dir] == "dir": print(f"{dir}\tfolder")
    print()
    for fil in sorted(entries):
        if entries[fil] == "file": print(f"{fil}\tfile")


    
if __name__ == "__main__":
    main()