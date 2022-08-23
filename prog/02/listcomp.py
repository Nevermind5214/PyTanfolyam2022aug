def f1():
    li = ['auto', 'villamos', 'metro']# → ['AUTO!', 'VILLAMOS!', 'METRO!']
    result = [s.upper() + "!" for s in li]
    print(result)

def f2():
    li = ['aladar', 'bela', 'cecil']# → ['Aladar', 'Bela', 'Cecil']
    result = [s.capitalize() for s in li]
    print(result)

def f3():
    result = [0 for i in range(10)]
    #result = [0] * 10
    print(result)
#, azaz inicializáljunk egy 10-elemű listát csupa 0-val.

def f4():
    #li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]# → [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    li = [i for i in range(1, 11)]
    #print(li)
    result = [n * 2 for n in li]
    print(result)
    
def f5():
    li = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']# → [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = [int(str) for str in li]
    print(result)
#(az első listában sztringek vannak)

def f6():
    num= "1234567"# → [1, 2, 3, 4, 5, 6, 7]#, vagyis van számunk sztring formátumban,
# s egy listába be akarjuk tenni a számjegyeit (számokként)
    result = [int(str) for str in list(num)]
    print(result)
    

def f7():
    sentence = 'The quick brown fox jumps over the lazy dog'
    result = [len(word) for word in sentence.split()]
    print(result)
# → [3, 5, 5, 3, 5, 4, 3, 4, 3], vagyis állapítsuk meg az egyes szavak hosszát

def f8():
    sentence = "python is an awesome language"# → ['p', 'i', 'a', 'a', 'l'],
# vagyis egy sztring szavainak a kezdőbetűit gyűjtsük össze egy listában
    result = [word[0] for word in sentence.split()]
    print(result)

def f9():
    sentence = 'The quick brown fox jumps over the lazy dog'
# → [('The', 3), ('quick', 5), ('brown', 5), ('fox', 3), ('jumps', 5), ('over', 4), ('the', 3), ('lazy', 4), ('dog', 3)], 
#vagyis a listában tuple-öket helyezzünk el a következő szerkezettel: (szó, szóhossz).
    result = [(word, len(word)) for word in sentence.split()]
    print(result)

def f10():
#[0, 2, 4, 6, 8]#, vagyis állítsuk elő egy listában a 10-nél kisebb páros számokat
    result = [n for n in range(0, 10, 2)]
    print(result)
 
def f11():
#11. feladat
#Vegyük a 20-nál kisebb számokat s állítsuk elő ezeknek a négyzetét.
#Ezen négyzetszámok közül csak a párosakat hagyjuk meg ([0, 4, 16, 36, 64, 100, 144, 196, 256, 324]).
    result = [n**2 for n in range(0, 20) if n**2 % 2 == 0]
    print(result)

def f12():
#12. feladat
#Vegyük a 20-nál kisebb számokat s állítsuk elő ezeknek a négyzetét.
#Ezen négyzetszámok közül csak azokat hagyjuk meg, melyeknek az utolsó számjegye "4" ([4, 64, 144, 324]).
    result = [n**2 for n in range(0, 20) if str(n**2)[-1] == "4"]
    print(result)

def f13():
#13. feladat
#Gyűjtsük össze az angol ábécé nagybetűit egy listában (használjuk a chr függvényt), (chr(65 -  90)
# majd fűzzük össze az elemeket egyetlen sztringgé: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
    result = ""
    for c in range(65,91):
        result += chr(c)
    print(result)

def f14():
    li = [' apple ', ' banana ', ' kiwi']# → ['apple', 'banana', 'kiwi'],
# vagyis a listában lévő szavak elejéről és végéről távolítsuk el a whitespace karaktereket
    result = [word.strip() for word in li]
    print(result)

def f15():
    li = [1, 0, 1, 1, 0, 1, 0, 0]# → "10110100", vagyis a listában lévő számjegyeket fűzzük össze egy sztringgé
    result = ""
    for n in li:
        result += str(n)
    print(result)
    

def main():
    f1()
    f2()
    f3()
    f4()
    f5()
    f6()
    f7()
    f8()
    f9()
    f10()
    f11()
    f12()
    f13()
    f14()
    f15()
    
if __name__ == "__main__":
    main()