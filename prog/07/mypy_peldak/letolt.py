
import pyutils

def main() -> None:
    url = "https://www.python.org/"
    html: str = pyutils.get_page(url)
    print(html)

##############################################################################

if __name__ == "__main__":
    main()
