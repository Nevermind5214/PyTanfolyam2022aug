def main():
    d = { 'b':'beta','a':'alfa','g':'gamma' }

    for k in sorted(d.keys()):
        print(k, '->', d[k])

    for t in d.items():
        print(t)
    
    for k, v in d.items():
        print(k, '->', v)
    
if __name__ == "__main__":
    main()