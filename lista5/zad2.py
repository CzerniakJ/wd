class Kwadrat:
    def __init__(self,x):
        self.x=x
    def __add__(self,kwadrat):
        return Kwadrat(self.x + kwadrat.x)
    def __str__(self):
        return f'Kwadrat({self.x})'
k1 = Kwadrat(5)
k2 = Kwadrat(2)

k3 = k1 + k2
print(k3)