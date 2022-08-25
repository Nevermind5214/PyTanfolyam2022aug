
"""
loop(5)
-----
1 2 3 4 5

loop(5, debug=True)
------
# start loop
1 2 3 4 5
# end loop

"""

def loop(n, debug=False):
    if debug: print("# start loop")

    for i in range(1, 5+1):
        print(f"{i} ", end="")
    print()

    if debug: print("# end loop")

def main():
    loop(5)
    print("-" * 10)
    loop(5, debug=True)
    
if __name__ == "__main__":
    main()