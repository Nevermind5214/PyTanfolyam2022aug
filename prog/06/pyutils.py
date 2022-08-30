import urllib.request

def get_page(url):
    return urllib.request.urlopen(url).read().decode("utf-8")