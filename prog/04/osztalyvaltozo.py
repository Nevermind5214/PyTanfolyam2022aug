
class Proba:
    i = 123
    peldanyositasok_szama = 0

    def __init__(self):
        Proba.peldanyositasok_szama += 1

    def hello(self):
        print("Hello")

def main():
    print(Proba.i)
    #Proba.hello()
    p = Proba()
    print(Proba.peldanyositasok_szama)
    p.hello()
    
    q = Proba()
    r = Proba()
    print(Proba.peldanyositasok_szama)
    
if __name__ == "__main__":
    main()