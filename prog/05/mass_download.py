"""
mass download

Tömeges letöltést ("mass download") szeretnénk elkövetni.
A következő file-okat szeretnénk leszedni:
http://example.com/galleryFX/1.jpg
http://example.com/galleryFX/2.jpg
http://example.com/galleryFX/3.jpg
http://example.com/galleryFX/4.jpg
http://example.com/galleryFX/5.jpg
http://example.com/galleryFX/6.jpg
http://example.com/galleryFX/7.jpg
http://example.com/galleryFX/8.jpg
http://example.com/galleryFX/9.jpg
http://example.com/galleryFX/10.jpg
http://example.com/galleryFX/11.jpg
http://example.com/galleryFX/12.jpg
http://example.com/galleryFX/13.jpg
http://example.com/galleryFX/14.jpg
http://example.com/galleryFX/15.jpg
Írjunk egy szkriptet, ami a fenti kimenetet produkálja.

Tipp
Ha tényleg le akarjuk ezeket tölteni, akkor a következőképpen járjunk el:

$ ./url_generator.py >down.txt
$ wget -i down.txt
Nehezítés
A fájlnevekben a számok fixen 2 hosszúságúak:
http://example.com/galleryFX/01.jpg
http://example.com/galleryFX/02.jpg
http://example.com/galleryFX/03.jpg
http://example.com/galleryFX/04.jpg
http://example.com/galleryFX/05.jpg
http://example.com/galleryFX/06.jpg
http://example.com/galleryFX/07.jpg
http://example.com/galleryFX/08.jpg
http://example.com/galleryFX/09.jpg
http://example.com/galleryFX/10.jpg
http://example.com/galleryFX/11.jpg
http://example.com/galleryFX/12.jpg
http://example.com/galleryFX/13.jpg
http://example.com/galleryFX/14.jpg
http://example.com/galleryFX/15.jpg
Módosítsuk a letöltő-szkriptet ennek megfelelően!
"""

def main():
    template = "http://example.com/galleryFX/{:02}.jpg"
    start = 1
    end = 15
    for i in range(start, end + 1):
        print(template.format("0" + str(i)))



if __name__ == "__main__":
    main()