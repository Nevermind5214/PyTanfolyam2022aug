
def product(li: list[int]) -> int:
    p = 1
    for n in li:
        p *= n
    #
    return p


def main() -> None:
    numbers = [3, 2, 5, 2]
    # numbers = []
    result = product(numbers)
    print(result)    # 60

##############################################################################

if __name__ == "__main__":
    main()
