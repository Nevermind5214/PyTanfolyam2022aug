PI = 3.14159

def hello(name, color, obj):
    # geza, kek az eg!
    # C-ben:
    # printf("%s, %s az %s!\n", name, color, obj);
    
    # v1
    #print("{0}, {1} az {2}! Ki? {0}".format(name, color, obj))
    
    # v2
    #print("{}, {} az {}! Ki? {}".format(name, color, obj, name))
    
    # v3
    print("{n}, {c} az {o}! Ki? {n}".format(n = name.capitalize(), c = color, o = obj))
        
    # v4
    #print("1 + 1 = {1 + 1}")#1 + 1 = {1 + 1}
    #print(f"1 + 1 = {1 + 1}")#1 + 1 = 2
    #print(f"{name}, {color} az {obj}! Ki? {name}")

def main():
    hello("geza", "kek", "eg")
    print("-" * 40)
    hello("peti", "piros", "rozsa")
    print("-" * 40)
    #print("pí értéke: " + PI) hiba string concat számmal
    #print("pí értéke: " + str(PI))
    print(f"pí értéke: {PI}")
    print("py", 3)
    print("pí értéke: ", PI)
    
if __name__ == "__main__":
    main()