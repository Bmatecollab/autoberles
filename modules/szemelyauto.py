from modules.autok import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, ajtok_szama, szemelyek_szama, motor_meret):
        super().__init__(rendszam, tipus, berleti_dij)
        self.ajtok_szama = ajtok_szama
        self.szemelyek_szama = szemelyek_szama
        self.motor_meret = motor_meret

    def jarmu_info(self):
        return (f"Személyautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, "
                f"Ajtók: {self.ajtok_szama}, Személyek: {self.szemelyek_szama}, "
                f"Motor: {self.motor_meret}L, Díj: {self.berleti_dij} Ft/nap")
