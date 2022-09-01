
PI = 3.14159

def hello(name: str, color: str, obj: str) -> None:
    # geza, kek az eg!
    # C-ben:
    # printf("%s, %s az %s!\n", name, color, obj);
    # v1
    # print("{0}, {1} az {2}! Ki? {0}".format(name, color, obj))
    # v2
    # print("{}, {} az {}!".format(name, color, obj))
    # v3
    print("{name}, {c} az {o}!".format(name=name.capitalize(), c=color, o=obj))
    # v4
    # value = h()*g()+73434-z()
    # print(f"1 + 1 = {value}")
    # print(f"{name}, {color} az {obj}!")

def main() -> None:
    hello("geza", "kek", "eg")
    print("-" * 40)
    hello("peti", "piros", "auto")
    print("-" * 40)
    print(f"pi erteke: {PI}")
    print("pi erteke:", PI)

##############################################################################

if __name__ == "__main__":
    main()
