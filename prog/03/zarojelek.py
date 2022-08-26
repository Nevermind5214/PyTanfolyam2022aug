"""
Zárójelek

Legyen adott egy kifejezés, melyben számok, zárójelek, illetve operátorok szerepelnek. Minket most csak a zárójelek érdekelnek. Háromféle zárójel szerepelhet a kifejezésben: "{}", "()", "[]". Ha egy zárójelet megnyitunk, akkor a típusának megfelelő párral be is kell zárni. A zárójelek hatásköre nem keresztezheti egymást. A feladat: egy kifejezésről döntsük el a zárójelek alapján, hogy helyes-e vagy sem (a számokkal és az operátorokkal most ne foglalkozzunk).

Példa:

test("((5+3)*2+1)") == True
test("{[(3+1)+2]+}") == True
test("(3+{1-1)}") == False
test("[1+1]+(2*2)-{3/3}") == True
test("(({[(((1)-2)+3)-3]/3}-3)") == False
"""

def test(kif):
    joe = True
    jelek = {'{':0,'(':0,'[':0}
    zaro = {'}':'{',')':'(',']':'['}
    utsonyitott = []

    for char in kif:
        if char in jelek:
            jelek[char] += 1
            utsonyitott.append(char)
        if char in zaro:
            jelek[zaro[char]] -= 1
            if zaro[char] != utsonyitott.pop(): joe = False

    if sum(jelek.values()) != 0: joe = False
    return joe

def main():
    print(test("((5+3)*2+1)"))
    print(test("{[(3+1)+2]+}"))
    print(test("(3+{1-1)}"))
    print(test("[1+1]+(2*2)-{3/3}"))
    print(test("(({[(((1)-2)+3)-3]/3}-3)"))
    
if __name__ == "__main__":
    main()