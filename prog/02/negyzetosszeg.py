"""
Az első tíz természetes szám négyzetösszege:

1^2 + 2^2 + … + 10^2 = 385

Az első tíz természetes szám összegének a négyzete:

(1 + 2 + … + 10)^2 = 552 = 3025

Vagyis az első tíz természetes szám összegének a négyzete és az első tíz természetes szám négyzetösszege közti különbség: 3025 − 385 = 2640.

Számítsuk ki az első száz természetes szám összegének a négyzete és az első száz természetes szám négyzetösszege közti különbséget!
"""
def magicszamol(meddig):
    return sum([n for n in range(1,meddig+1)])**2-sum([n**2 for n in range(1,meddig+1)])

def main():
    print(magicszamol(10))
    print(magicszamol(100))
    
if __name__ == "__main__":
    main()