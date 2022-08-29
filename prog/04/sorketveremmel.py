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
        self._data = []

    def push(self, item):
        """Puts an element on top of the stack."""
        self._data.append(item)

    def pop(self):
        """Returns the last pushed element and removes it from the stack."""
        if self.is_empty():
            return None
        return self._data.pop()

    def is_empty(self):
        """Returns a bool depending on whether the stack is empty."""
        return self.size() == 0
    
    def size(self):
        """Returns the number of elements currently on stack."""
        return len(self._data)

    def __str__(self):
        """Returns elements currently on stack as a string."""
        return str(self._data)[:-1]


class MyQueue:
    """Queue implemented two stacks."""
    def __init__(self):
        """Creates two empty stacks for its elements when initialized."""
        self._be = Verem()
        self._ki = Verem()

    def append(self, item):
        """Puts an to the front of the queue."""
        self._be.push(item)

    def popleft(self):
        """Returns the earliest element inserted still in the queue and removes it."""
        if self.is_empty(): return None
        if self._ki.is_empty():
            while not self._be.is_empty():
                self._ki.push(self._be.pop())
        return self._ki.pop()

    def is_empty(self):
        """Returns a bool depending on whether the queue is empty."""
        return (self._be.is_empty() and self._ki.is_empty())

    def size(self):
        """Returns the number of elements currently in the queue."""
        return self.be.size() + self.ki.size()

    def __str__(self):
        """Returns elements currently in the queue as a string."""
        return str(list(reversed(self._be._data)) + self._ki._data)



def main():
    v = Verem()
    print(v)
    print(v.is_empty())
    v.push(11)
    v.push(12)
    v.push(13)
    print(v)
    print(v.pop())
    print(v)
    print(v.pop())
    print(v)
    print(v.pop())
    print(v)
    print(v.pop())

    print("-" * 10)

    q = MyQueue()
    q.append(1)
    q.append(2)
    q.append(3)
    print(q)
    print(q.popleft())
    print(q.popleft())
    q.append(4)
    print(q)
    print(q.popleft())
    print(q.popleft())
    q.append(5)
    q.append(6)
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())
    
if __name__ == "__main__":
    main()