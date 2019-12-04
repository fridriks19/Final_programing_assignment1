
from UI.makeUI import MakeUI
from UI.getUI import GetUI
from UI.changeUI import ChangeUI



class MainUI():
    def __init__(self):
        self.WITDH = 50
        self.BORDER = "*"
        self.QUIT = "'q' - Hætta"
        self.GO_BACK = "'r' - Til baka"
        self.PICK = "Veldu skipun:"
        self.USER_INPUT = ("Valin skipun: ")
                        #The main menu starts here"       
    ###########################################################################
    ############################### main menu #################################
    ###########################################################################
    def main_menu(self):
        user_input = ""
        while user_input != "q":
            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("NaN Air"))/2)*" " +  "NaN Air"  +   "\n" + self.BORDER * self.WITDH ) # prints the header 
            print(self.PICK + "\n")
            print(self.QUIT+ "\n\n")
            print("'1' - Breyta" + "\n" + "'2' - Nýskrá" + "\n" + "'3' - Sækja" + "\n")
            user_input = input(self.USER_INPUT).lower()
            print()
    ###########################################################################
    ############################### change sub menu ###########################
    ###########################################################################           
            if user_input == "1":
                next_page = ChangeUI()
                next_page.change_menu()


    ###########################################################################
    ############################### Make sub menu #############################
    ###########################################################################        
            if user_input == "2":
                next_page = MakeUI()
                next_page.make_menu()
                
    ###########################################################################
    ############################### get sub menu ##############################
    ###########################################################################
            if user_input == "3":
                next_page = GetUI()
                next_page.get_menu()

                    
        else:    # if the user presses q
            print("Logging out.....")
            return BORDER * WITDH 

ui = MainUI()
print(ui.main_menu())