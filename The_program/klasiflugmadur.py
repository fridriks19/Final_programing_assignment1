from klasiemployee import Starfsmadur

class Flugmadur(Starfsmadur):
    def __init__(self, empl_info_list, stodugildi, rettindi):
        Starfsmadur.__init__(self, empl_info_list)
        self.starfstitill = "Pilot"
        self.stodugildi = stodugildi
        self.rettindi = rettindi

    def __str__(self):
        prnt_str = Starfsmadur.__str__(self)
        prnt_str += self.starfstitill + "\n"
        prnt_str += self.stodugildi + "\n"
        prnt_str += self.rettindi + "\n"
        return prnt_str

list_1 = ["Eggert Orri Hermannsson", "290688-4189", "Dalsgerði", "865-8995", "865-8995", "eggerth19@ru.is"]
sm1 = Flugmadur(list_1, "Captain", "NAFokkerF100")
print(sm1)