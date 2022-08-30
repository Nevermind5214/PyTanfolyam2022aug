"""
Kis- és nagybetűk felcserélve

Játékos Jancsika már megint figyelmetlen volt. Angolból esszét kellett írnia a Python programozási nyelvről, s ehhez a fater "The Art of Unix Programming" c. könyvéből kimásolta az idevágó fejezetet. Viszont nagy igyekezetében nem vette észre, hogy az első paragrafus végén véletlenül lenyomta a Caps Lock billentyűt. Csak a végén döbbent rá, hogy baj van, de az egész szöveget már nem akarta újra bepötyögni. Egy kétségbeesett levélben elküldte nekünk a szöveget, s a segítségünket kéri. Az esszé beküldési határideje éjfél, s Jancsika levelét 23.40-kor kaptuk meg. Tudunk segíteni Jancsikának, hogy meglegyen az aláírása?

Megjegyzés: oldjuk meg Pythonban is a problémát, de gondolkozzunk el más megoldási lehetősége(ke)n is.

Tipp: nézzük meg, hogy egy sztringnek van-e valamilyen swap*() nevű függvénye…
"""
def uncaps(line):
    retval = line
    for chr in line:

def main():
    outtext = ""
    with open("kisnagycsere.txt", "r", encoding="utf8") as infile, open("cserelt.txt", "w") as outfile:
        for line in infile.readlines():
            capsline = False
            for word in line.split():
                if word[0].islower() and word[1:].isupper(): capsline = True
            if capsline:
                outtext += uncaps(line) + "\n"
            else: outtext += line + "\n"
        outfile.write(outtext)



if __name__ == "__main__": main()