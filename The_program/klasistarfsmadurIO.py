from klasiemployee import Starfsmadur
from klasiflugmadur import Flugmadur

empl_str = "9653,dfgh,Pilot,jhgfd,jhgfds,ghg,66"


open_file = open("crew2.csv", "a")
open_file.write(empl_str)
open_file.close()
