class gen1:
    def __init__(self, a):
        self.a = a
    def gen(self):
        for index in range(len(self.a)-1):
            yield self.a[index]

p1 = gen1("qwerty")
print(p1)