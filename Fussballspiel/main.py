class Spieler:
    anzahl_Spieler = 0
    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position
        ## andere attribute noch machen 
        Spieler.anzahl_Spieler+= 1

    def get_staerke(self):
        return self.__staerke
    
    def set_staerke(self, staerke):
        self.__staerke = staerke
        return
    
    

