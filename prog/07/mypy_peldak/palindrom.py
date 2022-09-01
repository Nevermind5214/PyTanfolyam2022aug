
def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def main() -> None:
    s = "apa"
    print(f"{s} palindrom?", is_palindrome(s))

##############################################################################

if __name__ == "__main__":
    main()
