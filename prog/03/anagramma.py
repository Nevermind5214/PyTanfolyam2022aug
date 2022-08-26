"""
Anagramma
Az anagramma a szójátékok egy fajtája, melyben értelmes szavak vagy mondatok betűinek
 sorrendjét úgy változtatjuk meg, hogy az eredmény szintén értelmes szó vagy mondat legyen.
Példák:
listen = silent
A gentleman = Elegant man
Clint Eastwood = Old west action
dormitory = dirty room
stb.
Írjunk egy függvényt, amely kap két sztringet, s eldönti, hogy a második szó az első szó anagrammája-e vagy sem.
(A kis- és nagybetűket nem muszáj megkülönböztetni, lásd a 2. példát).
A feladatot többféleképpen is meg lehet oldani. Van egy triviális módszer, de engem inkább a nemtriviális változat érdekelne.
Vagyis próbáljuk meg megoldani a feladatot legalább kétféleképpen!
Tipp
A 3. példában látható, hogy a szóközök nem számítanak, ill. nincs különbség a kis- és nagybetűk között.
Írjon egy olyan függvényt, ami kap egy sztringet, s visszaadja annak a normalizált alakját. Pl. normalize("Clint Eastwood") == "clinteastwood".
"""


def normalize(str=""):
    return "".join(str.lower().split())

def anagram(word1,word2):
    return sorted(normalize(word1)) == sorted(normalize(word2))

def main():
    print(normalize("Clint Eastwood"))
    print("listen = silent ?: ", anagram("listen","silent"))
    print("A gentleman = Elegant man ?: ", anagram("A gentleman","Elegant man"))
    print("Clint Eastwood = Old west action ?: ", anagram("Clint Eastwood","Old west action"))
    print("dormitory = dirty room ?: ", anagram("dormitory","dirty room"))
    print("ezrossz = dirty room ?: ", anagram("ezrossz","dirty room"))

if __name__ == "__main__":
    main()