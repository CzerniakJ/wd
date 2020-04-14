class samogloski:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        elif self.data[self.index] == ("a" or "ą" or "e" or "ę" or "i" or "o" or "u" or "y"):
            return self.data[self.index]
        self.index = self.index - 1
print([a for a in samogloski("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat.")])       