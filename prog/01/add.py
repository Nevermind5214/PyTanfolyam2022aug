import sys

def main():
    if len(sys.argv) != 3:
        print("Hiba! Pontosan két argukmentum kell", file=sys.stderr)
        sys.exit(1)
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    print(n1 + n2)
    
if __name__ == "__main__":
    main()