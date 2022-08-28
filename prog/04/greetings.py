
class Greetings:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi {0}!".format(self.name))

def main():
    g = Greetings("Alice")
    print(g.name)
    g.say_hi()
    
if __name__ == "__main__":
    main()