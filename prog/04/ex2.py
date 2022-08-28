#import isprime
from isprime import is_prime

def main():
    print(sum([n for n in range(200) if is_prime(n)]))
    
if __name__ == "__main__":
    main()