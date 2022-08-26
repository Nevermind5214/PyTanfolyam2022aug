#python reverse.py megfordit.py > forditott.py
import sys

def main():
    with open(sys.argv[1]) as f:
        print(f.read()[::-1])

##############################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("One parameter is required.")
        sys.exit(1)
    # else
    main()