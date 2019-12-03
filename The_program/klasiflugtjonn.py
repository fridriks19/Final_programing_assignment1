from klasiemployee import Starfsmadur

class Flugtjonn(Starfsmadur):
    def __init__(self, empl_info_list):
        Starfsmadur.__init__(self, empl_info_list)
        self.val[1] = "Cabincrew"
        self.val[3] = "N/A"
