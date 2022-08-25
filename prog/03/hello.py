def hello(name, repeat=1, postfix=""):
    for _ in range(1,repeat):
        print(name + postfix)


def main():
    #hello("Laci")
    #print("-" * 10)
    #hello("Anna", repeat=2)
    #print("-" * 10)
    #hello("Bela",repeat=3, postfix="!")
    #print("-" * 10)
    hello("Bela",postfix="!", repeat=3)
    hello("Bela",3 ,"!")
    #hello("Bela","!", 3) hiba, számít a sorrend
    
if __name__ == "__main__":
    main()