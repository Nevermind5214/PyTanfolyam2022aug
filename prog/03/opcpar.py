def greet(name, greetings="Hello"):
    print(f"{greetings} {name}!")


def main():
    greet("Laszlo")
    greet("Laszlo", greetings="Hola")
    greet("Laszlo", "Bonjour")
    
if __name__ == "__main__":
    main()