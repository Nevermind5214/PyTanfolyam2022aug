"""
A tester wants to select every fifth item in a tuple
for functional testing,
starting with the second item in the tuple and
ending at the ninth item in the tuple.

Help: the 9th item is NOT included
Help: expected output: ('2222', '7777')
"""

def main():
    products = ('1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999')
    print(products[1:8:5])
    tester = slice(1, 8 ,5)
    print(products[tester])

##############################################################################

if __name__ == "__main__":
    main()
