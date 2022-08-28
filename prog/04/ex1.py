import isprime
#from isprime import is_prime

def main():
    for n in range(100):
        if(isprime.is_prime(n)): print(n)
    
if __name__ == "__main__":
    main()