from klasiemployee import Starfsmadur
from klasiflugtjonn import Flugtjonn

flugtjonn_listi = []
nafn = input("Nafn: ")
kennitala = input("Kennitala: ")
flugtjonn_listi.append(kennitala)
flugtjonn_listi.append(nafn)
starfsheiti = ""
flugtjonn_listi.append(starfsheiti)
stodugildi = input("Stöðugildi: ")
flugtjonn_listi.append(stodugildi)
rettindi = "N/A"
flugtjonn_listi.append(rettindi)
heimilisfang = input("Heimilisfang: ")
flugtjonn_listi.append(heimilisfang)
simanr = input("Símanúmer: ")
flugtjonn_listi.append(simanr)
nyr_flugtjonn = Flugtjonn(flugtjonn_listi)

write_string = ""
for val in nyr_flugtjonn.values():
    write_string += val + ","
print(write_string)
