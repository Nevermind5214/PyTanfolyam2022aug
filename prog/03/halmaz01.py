"""
Legyen adott a következő lista: [5, 2, 3, 5, 1, 4, -200, 5, 1, 3, 2, 2, 5] . 
Távolítsuk el a duplikátumokat, vagyis egy elem csak 1x szerepeljen a listában. 
Az eredmény listában az elemek legyenek rendezve!
"""

def main():
    li = [5, 2, 3, 5, 1, 4, -200, 5, 1, 3, 2, 2, 5]
    li = sorted(set(li)) #sorted listát ad vissza, nem kell alakítani
    print(li)
    
if __name__ == "__main__":
    main()