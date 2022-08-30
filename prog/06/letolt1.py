import pyutils

def main():
    url="https://www.python.org/"
    html = pyutils.get_page(url)
    """
    response = urllib.request.urlopen(url)
    raw = response.read()
    #print(type(raw)) # -> bytes
    html = raw.decode("utf-8")
    print(type(html))
    #print(html)
    # """

    print(html)


if __name__ == "__main__": main()