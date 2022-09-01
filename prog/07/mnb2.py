import requests
from bs4 import BeautifulSoup

def get_soup(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    return soup

def main():
    url = "https://www.mnb.hu/arfolyamok"
    soup = get_soup(url)
    #print(soup)
    trs = soup.find_all("tr")
    for tr in trs:
        tds = tr.find_all("td")
        if len(tds) ==4:
            deviza = tds[0].text
            ertek = float(tds[3].text.replace(",","."))
            print(f"1 {deviza} = {ertek} Ft")



if __name__ == "__main__":
    main()