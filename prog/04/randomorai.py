import random

def shuffled(li):
    newlist = li.copy()
    random.shuffle(newlist)
    return newlist

def main():
    li = [3, 8, 2, 8, 4, 2, 1, 9]
    print(li)
    print(shuffled(li))
    print(li)
    
if __name__ == "__main__":
    main()