def main():
    f = open("out.txt", "w")
    print("Hello", file=f)
    print("World", file=f)
    print("2022", file=f)


    f.close()
    print("DONE")
    
if __name__ == "__main__":
    main()