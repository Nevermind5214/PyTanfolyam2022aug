
INPUT = "szoveg.txt"
OUTPUT = "masolat.txt"


def main():
    """ ÚJ JÓ CUCC
    with open(INPUT, "r") as f1, open (OUTPUT, "w") as to:
        for line in f1:
            to.write(line)
    """
    #régi módszer
    f1 = open(INPUT, "r")
    to = open(OUTPUT, "w")
    for line in f1:
        to.write(line)
    f1.close()
    to.close()

if __name__ == "__main__":
    main()