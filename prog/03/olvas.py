def main():
    f = open("szoveg.txt", "r")
    """
    for line in f:
        line = line.rstrip("\n")
        if line.endswith("."): print(line)
    """
    #lines = f.readlines()
    #print(lines)
    
    #tartalom = f.read()
    #print("'" + tartalom + "'")

    elso = f.readline() #soronként olvas
    print("'" + elso + "'")
    masodik = f.readline()
    print("'" + masodik + "'")

    f.close()
if __name__ == "__main__":
    main()