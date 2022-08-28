
class Hello:
    def create_name(self, name):
        self.name = name

    def display_name(self):
        return self.name

    def greet(self):
        print(f"Hello {self.name}!")


def main():
    h = Hello()
    h.create_name("Alice")
    print(h.display_name())
    h.greet()
    print(h.name)

if __name__ == "__main__":
    main()