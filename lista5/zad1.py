class material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc 
        self.szerokosc = szerokosc
    def konstruktor(self):
        return print("xD")
    def wyswietl_nazwe(self):
        print ("nazwa")
class ubrania:
    def __init__(self, rozmiar, kolor, dla_kogo):
        self.rozmiar = rozmiar
        self.kolor = kolor 
        self.dla_kogo = dla_kogo
    def wyswietl_dane(self):
        print ("Rozmiar: {self.rozmiar}, kolor:{self.kolor},dla_kogo: {self.dla_kogo}")
class sweter:
    def __init__(self, rodzaj_swetra):
        self.rodzaj_swetra = rodzaj_swetra
    def wyswietl_dane(self):
        print("rpdzaj: {self.rodzaj_swetra}")