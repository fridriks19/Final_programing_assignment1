WITDH = 30
HEADER_MAIN = "NaN AIR"  
HEADER_SUB_A = "Breyta" 
HEADER_SUB_B = "Nýskrá"
HEADER_SUB_C = "Sækja"
BORDER = "*"

CHANGE = "'1' - Breyta"
MAKE = "'2' - Nýskrá"
GET = "'3' - Sækja"
QUIT = "'q' - Hætta"
GO_BACK = "'r' - Til baka"
PICK = "Veldu skipun:"
USER_INPUT = ("Valin skipun: ")
EMPLOYEE = "'1' - Starfmann"
PLACE = "'2' - Áfangastað"
WORK_FLIGHT = "'3' - Vinnuferð"
AIRPLANE = "'4' - Flugvél"
WORK_TIME = "'5' - Vinnustund"
AIRPLANE_TYPE = "'5' - Flugvélategund"
FLIGHT_ATTEND = "'2' - Flugþjónn"
FLYER = "'1' - Flugmaður"
Name_Input = "Nafn: "
SSN_Input = "Kennitala: "
ADDRESS_Input = "Heimilisfang: "
GSM_Input = "GSM-Sími: "
EMAIL_Input = "Netfang: "

user = " "
########HEADER  main menu 
while user != "q":
    
    print(BORDER * WITDH +"\n" + int((WITDH - len(HEADER_MAIN))/2)*" " +  HEADER_MAIN  +   "\n" + BORDER * WITDH )
  
    print(PICK +"\n")
    print(QUIT+ "\n")
    print(CHANGE)
    print(MAKE)
    print(GET)
    print()
    user = input(USER_INPUT)
    print()

#If the user inputs 1 we go into the CHANGE menu 
    if user == "1":
        change_user = user 
        while change_user != "r":
            print(BORDER * WITDH +"\n" + int((WITDH - len(HEADER_SUB_A))/2)*" " +  HEADER_SUB_A  +   "\n" + BORDER * WITDH )
  
            print(PICK +"\n")
            print(QUIT+ " "*5 + GO_BACK +"\n")
            print(EMPLOYEE)
            print(PLACE)
            print(WORK_FLIGHT)
            print()
            user1 = input(USER_INPUT)
            print()


#if the user inputs 2 we go into the MAKE menu
    elif user == "2":
        make_user = user 
        while make_user != "r":
            print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_B))/2)*" " +  HEADER_SUB_B +   "\n" + BORDER * WITDH )
  
            print(PICK +"\n")
            print(QUIT+ " "*5 + GO_BACK +"\n")
            print(EMPLOYEE)
            print(PLACE)
            print(WORK_FLIGHT)
            print(AIRPLANE)
            print(AIRPLANE_TYPE)
            print()
            make_user = input(USER_INPUT)
            print()
            #The result of a choisen input 
            if make_user == "1":
                make_employee = make_user 
                while make_employee  != "r":
                    print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_B))/2)*" " +  HEADER_SUB_B +   "\n" + BORDER * WITDH )
  
                    print(PICK +"\n")
                    print(QUIT+ " "*5 + GO_BACK +"\n")
                    print(FLYER)
                    print(FLIGHT_ATTEND)
                    print()
                    make_employee  = input(USER_INPUT)
                    print()
            elif make_user == "2":
                make_place= make_user 
                while make_place != "r":
                    print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_B))/2)*" " +  HEADER_SUB_B +   "\n" + BORDER * WITDH )
  
                    print(PICK +"\n")
                    print(QUIT+ " "*5 + GO_BACK +"\n")
                    input()
                    print()
                    print()
                    make_place = input(USER_INPUT)
                    print()
            elif make_user == "3":
                make_work_flight = make_user 
                while make_work_flight != "r":
                    print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_B))/2)*" " +  HEADER_SUB_B +   "\n" + BORDER * WITDH )
  
                    print(PICK +"\n")
                    print(QUIT+ " "*5 + GO_BACK +"\n")
                    print(FLYER)
                    print(FLIGHT_ATTEND)
                    print()
                    make_work_flight  = input(USER_INPUT)
                    print()
            elif make_user == "3":
                make_airplane = make_user 
                while make_airplane  != "r":
                    print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_B))/2)*" " +  HEADER_SUB_B +   "\n" + BORDER * WITDH )
  
                    print(PICK +"\n")
                    print(QUIT+ " "*5 + GO_BACK +"\n")
                    print(FLYER)
                    print(FLIGHT_ATTEND)
                    print()
                    make_airplane  = input(USER_INPUT)
                    print()
            elif make_user == "3":
                make_airplane_type = make_user 
                while make_airplane_type  != "r":
                    print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_B))/2)*" " +  HEADER_SUB_B +   "\n" + BORDER * WITDH )
  
                    print(PICK +"\n")
                    print(QUIT+ " "*5 + GO_BACK +"\n")
                    print(FLYER)
                    print(FLIGHT_ATTEND)
                    print()
                    make_airplane_type  = input(USER_INPUT)
                    print()


#If the user inputs 3 we go into the GET menu
    elif user == "3":
        get_user = user 
        while get_user != "r":
            print(BORDER * WITDH +"\n" +  int((WITDH - len(HEADER_SUB_C))/2)*" " +  HEADER_SUB_C  +   "\n" + BORDER * WITDH )
  
            print(PICK +"\n")
            print(QUIT+ " "*5 + GO_BACK +"\n")
            print(EMPLOYEE)
            print(PLACE)
            print(WORK_FLIGHT)
            print(AIRPLANE)
            print(WORK_TIME)
            print()
            get_user = input(USER_INPUT)
            print()



