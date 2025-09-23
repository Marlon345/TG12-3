class Leser:
    def __init__(self, name):
        self.name = name
        self.adresse = None
        self.geburtsdatum = None 
        self.lesenummer = None
        self.leihbuch = None
        self.AbgabeTermin = None
        print("Definiere: Adresse, Geburtsdatum, Lesenummer, Leihbuch, Abgabetermin")
    def __str__(self):
        return ("Name: " + self.name)

p1 = Leser("Jan")

