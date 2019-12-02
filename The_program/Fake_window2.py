WITDH = 30
HEADER = " NaN AIR"   
BORDER = "*"
HEADER_MID = ((WITDH - len(HEADER))/2)

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

user = " "
########HEADER  main menu 
while user != "q":
    
    print(BORDER * WITDH +"\n" + int(HEADER_MID)*" " +  HEADER  +   "\n" + BORDER * WITDH )
  
    print(PICK +"\n")
    print(QUIT+ "\n")
    print(CHANGE)
    print(MAKE)
    print(GET)
    print()
    user = input(USER_INPUT)
    print()
    
    if user == "1":
        user1 = user 
        while user1 != "r":
            print(BORDER * WITDH +"\n" + int(HEADER_MID)*" " +  HEADER  +   "\n" + BORDER * WITDH )
  
            print(PICK +"\n")
            print(QUIT+ " "*5 + GO_BACK +"\n")
            print(EMPLOYEE)
            print(PLACE)
            print(WORK_FLIGHT)
            print()
            user1 = input(USER_INPUT)
            print()


    elif user == "2":
        user2 = user 
        while user2 != "r":
            print(BORDER * WITDH +"\n" + int(HEADER_MID)*" " +  HEADER  +   "\n" + BORDER * WITDH )
  
            print(PICK +"\n")
            print(QUIT+ " "*5 + GO_BACK +"\n")
            print(EMPLOYEE)
            print(PLACE)
            print(WORK_FLIGHT)
            print(AIRPLANE)
            print(AIRPLANE_TYPE)
            print()
            user2 = input(USER_INPUT)
            print()

    elif user == "3":
        user3 = user 
        while user3 != "r":
            print(BORDER * WITDH +"\n" + int(HEADER_MID)*" " +  HEADER  +   "\n" + BORDER * WITDH )
  
            print(PICK +"\n")
            print(QUIT+ " "*5 + GO_BACK +"\n")
            print(EMPLOYEE)
            print(PLACE)
            print(WORK_FLIGHT)
            print(AIRPLANE)
            print(WORK_TIME)
            print()
            user3 = input(USER_INPUT)
            print()



