class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Konstruktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)
    def dodaj(self):
        return self.x + self.y
    def pod(self):
        return 2*self.x

p1 = Point(1,2)
print(p1.counter)
p1.update(2)
print(p1.counter)
p1.update(p1.dodaj)
print(p1.counter)
p1.update(p1.pod)
print(p1.counter)
