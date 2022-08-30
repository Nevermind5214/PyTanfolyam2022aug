import json
from pprint import pprint

def main():
    fname = "person.json"
    with open(fname, "r") as f:
        d = json.load(f)

    #print(d["wife"]["age"])
    #pprint(d)

    d["wife"]["age"] = 20
    to = open("younger.json", "w")
    json.dump(d, to, indent=4)
    to.close()
    
if __name__ == "__main__":
    main()