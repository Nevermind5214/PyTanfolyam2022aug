import time

def main():
    for i in range(10):
        print(".", end="")
        time.sleep(0.2)
    
    print("Flush:")
    for i in range(10):
        print(".", end="", flush=True)
        time.sleep(0.2)
    
if __name__ == "__main__":
    main()