"""
Döntsük el egy magyar szóról, hogy milyen hangrendű (mély, magas, vegyes, vagy semmilyen hangrendű).

Ha egy szóban vmennyi magánhangzó mély hangrendű, akkor a szó mély hangrendű. Ha egy szóban vmennyi magánhangzó magas hangrendű, akkor a szó magas hangrendű.
Ha egy szóban mély és magas hangrendű magánhangzók is előfordulnak, akkor a szó vegyes hangrendű. Ha a szóban nincs egyetlen magánhangzó sem, akkor semmilyen hangrendű.

Mély hangrendű magánhangzók: a, á, o, ó, u, ú.

Magas hangrendű magánhangzók: e, é, i, í, ö, ő, ü, ű.

Példák

"ablak" → mély
"erkély" → magas
"kisvasút" → vegyes
"magas" → mély :)
"mély" → magas :)
"Pfffffff" → semmilyen
Egy szó hangrendjének az eldöntését egy függvénnyel valósítsuk meg! A függvény kapja meg a szót, majd adja vissza a 4 lehetséges válasz egyikét.

Segítség

A magas és mély magánhangzókat egy-egy sztringben is letárolhatjuk:

MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'
...
words = ["ablak", "erkély", "kisvasút", "magas", "mély"]
Tipp

A függvényünk 4 lehetséges értéket adhat vissza. A "magas", "mély", stb. sztringek visszaadása helyett mi mást lehetne visszaadni? Hogyan lehetne a függvényünket elegánsabban megoldani?
"""
def hangrend(word):
    hr = "semmilyen"#magas mely vegyes
    MELY_MGHK = 'aáoóuú'
    MAGAS_MGHK = 'eéiíöőüű'
    for char in word:
        if char in MELY_MGHK:
            if hr == "magas" or hr == "vegyes": hr = "vegyes"
            else: hr = "mely"
        if char in MAGAS_MGHK:
            if hr == "mely" or hr == "vegyes": hr = "vegyes"
            else: hr = "magas"
    return hr

def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pffffff"]
    for word in words:
        print(word, hangrend(word))
    
if __name__ == "__main__":
    main()