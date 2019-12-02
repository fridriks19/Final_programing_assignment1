from klasiemployee import Starfsmadur

class Flugtjonn(Starfsmadur):
    def __init__(self, empl_info_list, stodugildi):
        Starfsmadur.__init__(self, empl_info_list)
        self.starfstitill = "Flugþjónn"
        self.stodugildi = stodugildi
        self.rettindi = "N/A"

    def __str__(self):
        prnt_str = Starfsmadur.__str__(self)
        prnt_str += self.starfstitill + "\n"
        prnt_str += self.stodugildi + "\n"
        prnt_str += self.rettindi + "\n"
        return prnt_str

list_1 = ["Eggert Orri Hermannsson", "290688-4189", "Dalsgerði", "456-3179", "865-8995", "eggerth19@ru.is"]
sm1 = Flugtjonn(list_1, "Flight Service")
print(sm1)