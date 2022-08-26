"""
Mondat extra szóközök nélkül
Adott egy mondat, melyben a szavak között tetszőleges számú szóköz szerepelhet. Távolítsa el az extra szóközöket, vagyis két szó között csak egy szóköz szerepeljen.
Példa:
test('I  love   Python') == "I love Python"
"""

def test(szoveg):
    return " ".join(szoveg.split())

def main():
    print(test('I  love                Python')) # "I love Python"
    
if __name__ == "__main__":
    main()