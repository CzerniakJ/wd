class samogloski:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        self.index += 1
        if (self.data[self.index] == ("a" or "e" or  "i" or "o" or "u" or "y")):
            return self.data[self.index]

print([a for a in samogloski("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat.")])       