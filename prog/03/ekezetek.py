"""
Ékezetek eltávolítása
Vegyük például a következő szöveget:
"A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.
A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.
A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre."
Forrás: http://sportgeza.hu/futball/hirek/2012/09/10/a_katalan_zaszlo_szineiben_futballozik_a_jovo_szezonban_a_barcelona/.
Feladat: az összes ékezetes magánhangzóról távolítsuk el az ékezetet, vagyis a kimenet sima ASCII szöveg legyen:
"A katalan zaszlo, a Senyera szineit fogja viselni a kovetkezo ideny…
Segítség
Ha angol billentyűzetünk van, akkor itt lesznek az ékezetes magánhangzók: áéíóöőúüűÁÉÍÓÖŐÚÜŰ.
Ha kész vagyunk, akkor csináljuk meg úgy is, hogy dictionary-t használunk!
Frissítés (20211018)
Ha már tanultuk a szótár adatszerkezetet, akkor csak erre a változatra vagyok kíváncsi!
"""
TEXT ="A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata. A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során. A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre."

def convert(text):
    chars = {'á':'a','é':'e','í':'i','ó':'o','ö':'o','ő':'o','ú':'u','ü':'u','ű':'u','Á':'A','É':'E','Í':'I','Ó':'O','Ö':'O','Ő':'O','Ú':'U','Ü':'U','Ű':'U'}
    newtext = ""
    for ch in text:
        if ch in chars: newtext += chars[ch]
        else: newtext += ch
    return newtext

def main():
    print(TEXT)
    print("-" * 40)
    print(convert(TEXT))
    
if __name__ == "__main__":
    main()