import sys

def cat(fname):
    try:
        with open(fname) as f:
            content = f.read().rstrip("\n")
            print(content)
    except FileNotFoundError as e:
        print(f"--- I/O error: {fname} not found")
        print(e)
    else: # noexception
        print("# nem volt kivétel")
    finally:
        print("# vége")

def main():
    files = sys.argv[1:]
    for file in files:
        cat(file)
    
if __name__ == "__main__":
    main()