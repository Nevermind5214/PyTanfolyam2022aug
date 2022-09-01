
def get_movie_info() -> tuple[str, int, float]:#tuple[int, ...]:
    # kapcsolódás egy ab.-hoz
    # visszaadunk egy sort (rekordot)
    return ("Total Recall", 1990, 7.5)

def main() -> None:
    title, year, score = get_movie_info()
    print(title, year, score)

##############################################################################

if __name__ == "__main__":
    main()
