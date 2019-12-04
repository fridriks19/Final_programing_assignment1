#import 



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
                change_input = user_input   # til að maður geti bakkað um 1 í stað þess að quita bara 
                while change_input != "r":
                    print(BORDER * WITDH +"\n" + int((WITDH - len("Breyta"))/2)*" " +  "Breyta"  +   "\n" + BORDER * WITDH )
                    print(PICK +"\n")
                    print(QUIT+ " "*5 + GO_BACK +"\n")
                    print("'1' - Starfmann" + "\n" + "'2' - Áfangastað" + "\n" + "'3' - Vinnuferð" + "\n" + "'4' - Flugvél" + "\n" + "'5' - Flug/vinnutímar" + "\n")
                    change_input = input(USER_INPUT).lower()
                    print()
    #####///kalla síðan í change ui fyrir allt sem er mögulegt að velja hér fyrir ofan t.d Employees

    ###########################################################################
    ############################### Make sub menu #############################
    ###########################################################################        
            if user_input == "2":
                make_input = user_input
                while make_input != "r":
                    print(BORDER * WITDH +"\n" + int((WITDH - len("Nýskrá"))/2)*" " +  "Nýskrá"  +   "\n" + BORDER * WITDH )
                    print(PICK +"\n")
                    print(QUIT+ " "*5 + GO_BACK +"\n")
                    print("'1' - Starfmann" + "\n" + "'2' - Áfangastað" + "\n" + "'3' - Vinnuferð" + "\n" + "'4' - Flugvél" + "\n" + "'5' - Flug/vinnutímar" + "\n")
                    make_input = input(USER_INPUT).lower()
                    print()


    ###########################################################################
    ############################### get sub menu ##############################
    ###########################################################################
            if user_input == "3":
                get_input = user_input
                while get_input != "r":
                    print(BORDER * WITDH +"\n" + int((WITDH - len("Sækja"))/2)*" " +  "Sækja"  +   "\n" + BORDER * WITDH )
                    print(PICK +"\n")
                    print(QUIT+ " "*5 + GO_BACK +"\n")
                    print("'1' - Starfmann" + "\n" + "'2' - Áfangastað" + "\n" + "'3' - Vinnuferð" + "\n" + "'4' - Flugvél" + "\n" + "'5' - Flug/vinnutímar" + "\n")
                    get_input = input(USER_INPUT)
                    print()
        else:    # if the user presses q
            print("Logging out.....")
            return BORDER * WITDH 

ui = MainUI()
print(ui.main_menu())