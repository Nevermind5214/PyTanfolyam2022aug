"""
Sor adatszerkezet két veremmel
Írjunk egy MyQueue nevű osztályt, amely egy sor adatszerkezetet implementál két verem felhasználásával.
Vagyis az osztályon belül legyen két verem, de maga az osztály kívülről úgy működjön, mint egy sor.
Valójában az osztálynak egy sor adatszerkezetet kell megvalósítania, de mi az implementáció során ezt 2 db veremmel akarjuk megoldani.
(Papíron gondolják át, hogy ez hogyan lehetséges).

Az osztály támogassa a köv. műveleteket:

append: beszúrás a sor végére
popleft: térjen vissza a sor első elemével (s ezt az elemet vegye is ki a sorból)
is_empty: üres-e a sor
size: a sorban lévő elemek száma
A két verem esetén csakis a szabályos veremműveletek használhatók!
Vagyis új elem berakása a verem tetejére, ill. a legfelül lévő elem eltávolítása.
Akár az órán vett Verem implementációt is lehet használni!
"""

class Verem:
    """Stack implemented using a list."""
    def __init__(self):
        """Creates an empty list for its elements when initialized."""
        self.elemek = []

    def push(self, elem):
        """Puts an element on top of the stack."""
        self.elemek.append(elem)

    def pop(self):
        """Returns the last pushed element and removes it from the stack."""
        return self.elemek.pop()

    def is_empty(self):
        """Returns a bool depending on whether the stack is empty."""
        return self.size() == 0
    
    def size(self):
        """Returns the number of elements currently on stack."""
        return len(self.elemek)


class MyQueue:
    """Queue implemented two stacks."""
    def __init__(self):
        """Creates two empty stacks for its elements when initialized."""
        self.be = Verem()
        self.ki = Verem()

    def append(self, elem):
        """Puts an to the front of the queue."""
        self.be.push(elem)

    def popleft(self,):
        """Returns the earliest element inserted still in the queue and removes it."""
        if self.ki.is_empty():
            while not self.be.is_empty():
                self.ki.push(self.be.pop())
        return self.ki.pop()

    def is_empty(self,):
        """Returns a bool depending on whether the queue is empty."""
        return (self.be.is_empty() and self.ki.is_empty())

    def size(self,):
        """Returns the number of elements currently in the queue."""
        return self.be.size() + self.ki.size()



def main():
    q = MyQueue()
    q.append(1)
    q.append(2)
    q.append(3)
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())
    q.append(4)
    print(q.popleft())
    q.append(5)
    q.append(6)
    print(q.popleft())
    print(q.popleft())
    
if __name__ == "__main__":
    main()