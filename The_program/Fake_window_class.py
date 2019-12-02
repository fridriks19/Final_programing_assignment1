WITDH = 30
HEADER_MAIN = "NaN AIR"  
HEADER_SUB_A = "Breyta" 
HEADER_SUB_B = "Nýskrá"
HEADER_SUB_C = "Sækja"
BORDER = "*"

#Fastir strengir
QUIT = "'q' - Hætta"
GO_BACK = "'r' - Til baka"
SAVE = "'s' - Vista upplýsingar"
PICK = "Veldu skipun:"
USER_INPUT = ("Valin skipun: ")
#Forsíða 
CHANGE = "'1' - Breyta"
MAKE = "'2' - Nýskrá"
GET = "'3' - Sækja"
#Sub síður
EMPLOYEE = "'1' - Starfmann"
PLACE = "'2' - Áfangastað"
WORK_FLIGHT = "'3' - Vinnuferð"
AIRPLANE = "'4' - Flugvél"
WORK_TIME = "'5' - Vinnustund"
AIRPLANE_TYPE = "'5' - Flugvélategund"
FLIGHT_ATTEND = "'2' - Flugþjónn"
FLYER = "'1' - Flugmaður"

#Input síður#
NAME_INPUT = "Nafn: "
SSN_INPUT  = "Kennitala: "
ADDRESS_INPUT  = "Heimilisfang: "
GSM_INPUT  = "GSM-Sími: "
EMAIL_INPUT  = "Netfang: "
#Áfangastaðir
LAND_INPUT = "Land: "
AIRPORT_INPUT = "Flugvöllur: "
FLIGHT_TIME_INPUT = "Flugtími: "
DISTANCE_INPUT = "Fjarlægð"
CONTACT_INPUT = "Tengiliður"
EMERGENCY_PHONE_INPUT = "Neyðarsími"



class Menu():
    def __init__(self):
        self.user_input = USER_INPUT
    
    def __str__(self):
        print(BORDER * WITDH +"\n" + int((WITDH - len(HEADER_MAIN))/2)*" " +  HEADER_MAIN  +   "\n" + BORDER * WITDH )
        print(PICK +"\n")
        print(QUIT+ "\n\n" + CHANGE + "\n" + MAKE + "\n" + GET + "\n")
        self.user_input = input(USER_INPUT)
        print()
        return self.user_input

class Change(Menu):
    def __init__(self):
        pass

    def __str__(self):
        pass

class Make(Menu):
    def __init__(self):
        self.user_input

    def __str__(self):
        return "aids"

class Get(Menu):
    def __init__(self):
        pass




def main():
    command = Menu()
    while command != "q":
        if command == "1":
            command = Change()

        if command == "2": 
            print("make")
            command = Make()
            print(command)

        if command == "3":
            command = Get()
    else:
        print("Turning off!")
main()