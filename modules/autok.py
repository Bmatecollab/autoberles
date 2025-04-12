from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij

    @abstractmethod
    def jarmu_info(self):
        pass

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, ajtok_szama):
        super().__init__(rendszam, tipus, berleti_dij)
        self.ajtok_szama = ajtok_szama

    def jarmu_info(self):
        return f"Személyautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Ajtók: {self.ajtok_szama}, Díj: {self.berleti_dij} Ft/nap"

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras = teherbiras

    def jarmu_info(self):
        return f"Teherautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Teherbírás: {self.teherbiras} kg, Díj: {self.berleti_dij} Ft/nap"
