class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


print([a for a in Wspak("przyklad1")])
print([b for b in Wspak("Ala ma kota")])
print([c for c in Wspak("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat.")])