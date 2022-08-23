"""
többsoros komment

else if -> elif
"""

import sys

def hello(nev):
    if nev == "batman" or nev == "robin":
        print("Denevérveszély!")
    else:
        print("Helló " + nev + "!")

def main():
    name = sys.argv[1]
    hello(name)
    
if __name__ == "__main__":
    main()