#!/usr/bin/env python3

import sys

def is_palindrome(s):
    return s == s[::-1]

def is_palindrome2(s):
    i = 0
    while i < len(s):
        if s[i] != s[-(i+1)]: return False
        i += 1
    return True

def is_palindrome3(s):
    if len(s) > 0:
        return s[0] == s[-1] and is_palindrome3(s[1:-1])
    else: return True

def main():
    s = sys.argv[1]
    print(f"{s} palindróm? {is_palindrome(s)}")
    print(f"{s} palindróm? {is_palindrome2(s)}")
    print(f"{s} palindróm? {is_palindrome3(s)}")
    
if __name__ == "__main__":
    main()