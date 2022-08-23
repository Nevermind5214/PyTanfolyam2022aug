#!/usr/bin/env python3

def prod(li):
    p = 1
    for n in li:
        p *= n
    return p

def main():
    nums = [3, 2, 5, 2]
    result = prod(nums)
    print(result)   # 60
    
if __name__ == "__main__":
    main()