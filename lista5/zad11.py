class FibIterator:

    def __init__(self, n):
        self.n = n
        self.i = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration

        self.i += 1
        self.a, self.b = self.b, self.a + self.b
        return self.a

print([a for a in FibIterator(10)]) 