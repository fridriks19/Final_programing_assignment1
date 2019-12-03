from klasiemployee import Starfsmadur

class Flugmadur(Starfsmadur):
    def __init__(self, empl_info_list):
        Starfsmadur.__init__(self, empl_info_list)
        self.val[1] = "Pilot"
