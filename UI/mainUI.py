from UI.getUI import GetUI
from UI.makeUI import MakeUI
from UI.changeUI import ChangeUI



WITDH = 50
BORDER = "*"
QUIT = "'q' - Hætta"
GO_BACK = "'r' - Til baka"
PICK = "Veldu skipun:"
USER_INPUT = ("Valin skipun: ")



class MainUI():
    def __init__(self):
        pass

                        #The main menu starts here"       
    ###########################################################################
    ############################### main menu #################################
    ###########################################################################
    def main_menu(self):
        user_input = ""
        while user_input != "q":
            print(BORDER * WITDH +"\n" + int((WITDH - len("NaN Air"))/2)*" " +  "NaN Air"  +   "\n" + BORDER * WITDH ) # prints the header 
            print(PICK + "\n")
            print(QUIT+ "\n\n")
            print("'1' - Breyta" + "\n" + "'2' - Nýskrá" + "\n" + "'3' - Sækja" + "\n")
            user_input = input(USER_INPUT).lower()
            print()
    ###########################################################################
    ############################### change sub menu ###########################
    ###########################################################################           
            if user_input == "1":
                next_page = ChangeUI()


    ###########################################################################
    ############################### Make sub menu #############################
    ###########################################################################        
            if user_input == "2":
                next_page = MakeUI()
                
    ###########################################################################
    ############################### get sub menu ##############################
    ###########################################################################
            if user_input == "3":
                next_page = GetUI()

                    
        else:    # if the user presses q
            print("Logging out.....")
            return BORDER * WITDH 

ui = MainUI()
print(ui.main_menu())