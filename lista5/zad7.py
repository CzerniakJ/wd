class Wi:
    def __init__(self, a):
        self.a = a
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index  == len(self.a):
            raise StopIteration
        elif self.index % 2 == 0:
            return self.a[self.index]
        self.index = self.index + 1
        


print([a for a in Wi("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat.")])       