from klasiemployee import Starfsmadur
from klasiflugmadur import Flugmadur

flugmadur_listi = []
nafn = input("Nafn: ")
kennitala = input("Kennitala: ")
flugmadur_listi.append(kennitala)
flugmadur_listi.append(nafn)
starfsheiti = ""
flugmadur_listi.append(starfsheiti)
stodugildi = input("Stöðugildi: ")
flugmadur_listi.append(stodugildi)
rettindi = input("Réttindi á hvaða týpu flugvéla: ")
flugmadur_listi.append(rettindi)
heimilisfang = input("Heimilisfang: ")
flugmadur_listi.append(heimilisfang)
simanr = input("Símanúmer: ")
flugmadur_listi.append(simanr)
nyr_flugmadur = Flugmadur(flugmadur_listi)

