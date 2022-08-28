from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

def main():
    print(Direction.UP)
    print(type(Direction.UP))
    print(Direction.UP.name)
    print(Direction.UP.value)
    
if __name__ == "__main__":
    main()