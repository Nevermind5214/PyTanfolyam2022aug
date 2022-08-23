#!/usr/bin/env python3

def ford(s):
    return s[::-1]

def fordit(n):
    return int(str(n)[::-1])

def main():
    szam = input("Szám: ")
    print(ford(szam))
    print(fordit(szam))
    
if __name__ == "__main__":
    main()