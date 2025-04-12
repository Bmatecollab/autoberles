import sys
sys.path.append('./')
from modules.autokolcsonzo import Autokolcsonzo
from modules.autok import Szemelyauto, Teherauto

def teszt_adatok_betoltese():
    kolcsonzo = Autokolcsonzo("GDE Autókölcsönző")

    auto1 = Szemelyauto("ABC123", "Toyota Corolla", 10000, 4)
    auto2 = Szemelyauto("XYZ789", "Ford Focus", 9500, 5)
    auto3 = Teherauto("DEF456", "Mercedes Sprinter", 15000, 2000)

    kolcsonzo.hozzaad_auto(auto1)
    kolcsonzo.hozzaad_auto(auto2)
    kolcsonzo.hozzaad_auto(auto3)

    kolcsonzo.auto_berles("ABC123", "Kiss Gábor", "2025-04-15", "2025-04-17")
    kolcsonzo.auto_berles("DEF456", "Nagy Anna", "2025-04-18", "2025-04-20")
    kolcsonzo.auto_berles("XYZ789", "Tóth Péter", "2025-04-19", "2025-04-19")

    return kolcsonzo


def menu():
    kolcsonzo = teszt_adatok_betoltese()

    while True:
        print("\n--- Autókölcsönző Menü ---")
        print("1. Autók listázása")
        print("2. Autó bérlése")
        print("3. Bérlés lemondása")
        print("4. Aktív bérlések")
        print("0. Kilépés")

        valasztas = input("Válassz egy opciót: ")

        if valasztas == "1":
            print("\nAutók:")
            print(kolcsonzo.listaz_autok())

        elif valasztas == "2":
            rendszam = input("Add meg az autó rendszámát: ")
            berlo = input("Add meg a neved: ")
            kezdet = input("Add meg a bérlés kezdő dátumát (YYYY-MM-DD): ")
            veg = input("Add meg a bérlés vég dátumát (YYYY-MM-DD): ")
            print(kolcsonzo.auto_berles(rendszam, berlo, kezdet, veg))

        elif valasztas == "3":
            rendszam = input("Add meg a rendszámot: ")
            berlo = input("Add meg a neved: ")
            print(kolcsonzo.berles_lemondas(rendszam, berlo))

        elif valasztas == "4":
            print("\nAktív bérlések:")
            print(kolcsonzo.listaz_berlesek())

        elif valasztas == "0":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen opció.")


if __name__ == "__main__":
    menu()
