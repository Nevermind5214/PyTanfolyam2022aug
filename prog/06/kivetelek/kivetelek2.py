#!/usr/bin/env python3

"""
Több finally ág nem lehet, csak max. 1 db.

Viszont! A try után el lehet hagyni az except-et, az nem kötelező.

A try után vagy except jön, vagy finally. Különben hiba.
"""

def main():
    a = 5
    b = 2
    try:
        result = a / b
        print(result)
    finally:
        print("END")

##############################################################################

if __name__ == "__main__":
    main()
