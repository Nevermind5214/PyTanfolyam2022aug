import requests

def main():
    url = "https://jsonip.com/"
    r = requests.get(url)
    d = r.json()
    ip = d["ip"]
    print(f"Az Ön IP címe: {ip}")
    
if __name__ == "__main__":
    main()