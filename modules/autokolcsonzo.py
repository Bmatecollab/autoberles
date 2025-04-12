from modules.berles import Berles
from datetime import datetime

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def hozzaad_auto(self, auto):
        self.autok.append(auto)

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

        for auto in self.autok:
            if auto.rendszam == rendszam:
                if self.auto_elofoglalt(auto, kezdet, veg):
                    return "Ez az autó már foglalt ebben az időszakban."
                berles = Berles(auto, berlo_nev, kezdet, veg)
                self.berlesek.append(berles)
                return (f"Bérlés sikeres {berlo_nev} részére {kezdet_str} és {veg_str} között. "
                        f"Összeg: {auto.berleti_dij * berles.napok_szama()} Ft ({berles.napok_szama()} nap)")

        return "Nincs ilyen autó."

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
        return "\n".join(auto.jarmu_info() for auto in self.autok)
