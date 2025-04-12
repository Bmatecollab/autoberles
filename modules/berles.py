from datetime import datetime

class Berles:
    def __init__(self, auto, berlo_nev, kezdet, veg):
        self.auto = auto
        self.berlo_nev = berlo_nev
        self.kezdet = kezdet
        self.veg = veg

    def napok_szama(self):
        return (self.veg - self.kezdet).days + 1

    def __str__(self):
        return (f"{self.berlo_nev} bérelte {self.auto.rendszam} ({self.auto.tipus}) autót "
                f"{self.kezdet.strftime('%Y-%m-%d')} - {self.veg.strftime('%Y-%m-%d')} között, "
                f"{self.napok_szama()} napra - Ár: {self.auto.berleti_dij * self.napok_szama()} Ft")
