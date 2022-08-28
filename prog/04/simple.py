
class EmptyClass:
    pass

class MyClass:
    def hello(self):
        return "Hello World!"


def main():
    o = MyClass()
    print(o.hello())
    
if __name__ == "__main__":
    main()