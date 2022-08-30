#!/usr/bin/env python3

def main():
    a = 5
    b = 2

    try:
        result = a / b
        print(f"{result=}")
    except:
        print("Hopp! Kivétel!")
    else:
        print("minden oké")
    finally:
        print("END")

##############################################################################

if __name__ == "__main__":
    main()
