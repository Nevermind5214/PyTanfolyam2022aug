import re

#re.search(pat, text)

def main():
    match = re.search("reg.", "reggeli és regularis kifejezesek")
    if match:
        print(str(match.group()))
        #m.group() #->object
    """m = re.search("linux", "regularis kifejezesek")
    m.group()"""

if __name__ == "__main__": main()