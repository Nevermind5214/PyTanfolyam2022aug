def main():
    f = open("out2.txt", "w")
    print("hello", file=f)
    f.write("py")
    f.write("thon\n")


    f.close()
    print("DONE")
    
if __name__ == "__main__":
    main()