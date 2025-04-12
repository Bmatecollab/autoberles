from modules.berles import Berles
from datetime import datetime

class SzemelyautoKezelo:
    def __init__(self):
        self.autok = []

    def hozzaad(self, auto):
        self.autok.append(auto)

    def listaz(self):
        return "\n".join(auto.jarmu_info() for auto in self.autok)

    def keres(self, rendszam):
        return next((auto for auto in self.autok if auto.rendszam == rendszam), None)

class TeherautoKezelo:
    def __init__(self):
        self.autok = []

    def hozzaad(self, auto):
        self.autok.append(auto)

    def listaz(self):
        return "\n".join(auto.jarmu_info() for auto in self.autok)

    def keres(self, rendszam):
        return next((auto for auto in self.autok if auto.rendszam == rendszam), None)

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.szemelyautok = SzemelyautoKezelo()
        self.teherautok = TeherautoKezelo()
        self.berlesek = []

    def osszes_auto(self):
        return self.szemelyautok.autok + self.teherautok.autok

    def auto_elofoglalt(self, auto, kezdet, veg):
        for berles in self.berlesek:
            if berles.auto.rendszam == auto.rendszam:
                if kezdet <= berles.veg and veg >= berles.kezdet:
                    return True
        return False

    def auto_berles(self, rendszam, berlo_nev, kezdet_str, veg_str):
        try:
            kezdet = datetime.strptime(kezdet_str, "%Y-%m-%d")
            veg = datetime.strptime(veg_str, "%Y-%m-%d")
        except ValueError:
            return "Hibás dátumformátum! Használj YYYY-MM-DD formátumot."

        if veg < kezdet:
            return "A végdátum nem lehet korábbi, mint a kezdődátum."

        auto = self.szemelyautok.keres(rendszam) or self.teherautok.keres(rendszam)
        if not auto:
            return "Nincs ilyen autó."

        if self.auto_elofoglalt(auto, kezdet, veg):
            return "Ez az autó már foglalt ebben az időszakban."

        berles = Berles(auto, berlo_nev, kezdet, veg)
        self.berlesek.append(berles)
        return (f"Bérlés sikeres {berlo_nev} részére {kezdet_str} és {veg_str} között. "
                f"Összeg: {auto.berleti_dij * berles.napok_szama()} Ft ({berles.napok_szama()} nap)")

    def berles_lemondas(self, rendszam, berlo_nev):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.berlo_nev == berlo_nev:
                self.berlesek.remove(berles)
                return "Bérlés lemondva."
        return "Nincs ilyen bérlés."

    def listaz_berlesek(self):
        if not self.berlesek:
            return "Nincs aktív bérlés."
        return "\n".join(str(berles) for berles in self.berlesek)

    def listaz_autok(self):
        autok = self.osszes_auto()
        return "\n".join(auto.jarmu_info() for auto in autok)
