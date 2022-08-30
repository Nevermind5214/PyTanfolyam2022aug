import json, requests

def main():
    url = "https://jsonip.com/"
    r = requests.get(url)
    data = r.text
    ipdict = json.loads(data)
    ip = ipdict["ip"]
    print(f"Az Ön IP címe: {ip}")
    
if __name__ == "__main__":
    main()