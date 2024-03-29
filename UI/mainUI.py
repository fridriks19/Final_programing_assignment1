
from UI.makeUI import MakeUIupd
from UI.getUI import GetUI
from UI.changeUI import ChangeUI
import time
import sys

def animate():
    ''' Makes a cool little animation when the user closes the program'''
    for i in range(0,4):
        sys.stdout.write('\rLogging Out |')
        time.sleep(0.1)
        sys.stdout.write('\rLogging Out /')
        time.sleep(0.1)
        sys.stdout.write('\rLogging Out -')
        time.sleep(0.1)
        sys.stdout.write('\rLogging Out \\')
        time.sleep(0.1)
    sys.stdout.write('\rSuccess!     ')
    time.sleep(0.3)
    input("Press 'Enter' key to exit ")


class MainUI():
    def __init__(self):
        ''' This is the main user interface and here the user can choose what main action he whants to do
            change something, get/see some information or make/add something new to the system'''
        self.__change = ChangeUI()
        self.__get = GetUI()
        self.__make = MakeUIupd()
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
                self.__change.change_menu()


    ###########################################################################
    ############################### Make sub menu #############################
    ###########################################################################        
            if user_input == "2":
                self.__make.make_menu()
                
    ###########################################################################
    ############################### get sub menu ##############################
    ###########################################################################
            if user_input == "3":
                self.__get.get_menu()

                    
        else:    # if the user presses q
            #print("Logging out.....")
            animate()
            print()
            return self.BORDER * self.WITDH 
