#!/usr/bin/env python3

def main():
    li = ["alfa", "beta", "gamma"]
    
    cnt = 0
    for index, value in enumerate(li, start=5):
        print(index, value)
    
if __name__ == "__main__":
    main()