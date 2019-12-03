from klasiemployee import Starfsmadur
from klasiflugmadur import Flugmadur


empl_str = "9653,dfgh,Pilot,jhgfd,jhgfds,ghg,66"

class StarfsmadurIO:
    def __init__(self, empl_str):
        self.empl_str = empl_str
    
    def save_employee(self):
        open_file = open("crew2.csv", "a")
        open_file.write(self.empl_str)
        open_file.close()
        return "Starfsmaður vistaður"

S1 = StarfsmadurIO(empl_str)
print(S1.save_employee())
