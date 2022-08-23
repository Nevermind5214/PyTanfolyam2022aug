def get_movie_info():
    # kapcsolódás adatbázishoz
    # visszaadunk egy sort(rekordot)
    return ("Total Recall", 1990, 7.5)

def main():
    title, year, score = get_movie_info()
    #title = t[0]
    #year = t[1]
    #score = t[2]
    print(title, year, score)
    
if __name__ == "__main__":
    main()