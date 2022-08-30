#!/usr/bin/env python3

"""
raise : a legutóbbi kivétel obj.-ot (újra) eldobja
"""

def main():
    a = 5
    b = 0
    try:
        result = a / b
        print(result)
    except Exception as e:
        print(e)
        raise
    finally:
        print("END")

##############################################################################

if __name__ == "__main__":
    main()
