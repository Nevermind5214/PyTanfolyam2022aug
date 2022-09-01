import requests
from bs4 import BeautifulSoup

def get_soup(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    return soup

def main():
    #url = "https://www.mnb.hu/arfolyamok"
    url = "https://www.python.org/"
    soup = get_soup(url)
    #print(soup)
    title = soup.find("title")
    if title:
        #print(title)
        value = title.text.strip()
        print("'" + value + "'")


if __name__ == "__main__":
    main()