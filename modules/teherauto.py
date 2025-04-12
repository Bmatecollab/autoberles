from modules.autok import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras, motor_meret):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras = teherbiras
        self.motor_meret = motor_meret

    def jarmu_info(self):
        return (f"Teherautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, "
                f"Teherbírás: {self.teherbiras} kg, Motor: {self.motor_meret}L, "
                f"Díj: {self.berleti_dij} Ft/nap")
