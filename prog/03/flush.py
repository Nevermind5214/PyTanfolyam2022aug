import time

def main():
    print("Default:")
    for i in range(10):
        print(".", end="")
        time.sleep(0.2)
    
    print("\nFlush:")
    for i in range(10):
        print(".", end="", flush=True)
        time.sleep(0.2)
    
if __name__ == "__main__":
    main()