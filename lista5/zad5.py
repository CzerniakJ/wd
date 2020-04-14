class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        # lub
        # super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

print(issubclass(Pracownik, Osoba))
print(issubclass(Pracownik, Menadzer))
print(issubclass(Pracownik, Pracownik))
print(isinstance(Pracownik, Osoba))
print(isinstance(Pracownik, Pracownik))
print(isinstance(Pracownik, Menadzer))
print(issubclass(Menadzer, Osoba))
print(issubclass(Menadzer, Menadzer))
print(issubclass(Menadzer, Pracownik))
print(isinstance(Menadzer, Osoba))
print(isinstance(Menadzer, Pracownik))
print(isinstance(Menadzer, Menadzer))