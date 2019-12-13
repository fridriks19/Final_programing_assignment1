 
            if get_input == "4":    # Get one employee by his ssn number and the user inputs the ssn
                print()
                print(self.GO_BACK +"\n") 
                employee_ssn_input = ""
                while employee_ssn_input != "r":
                    employee_ssn_input = input("Kennitala starfsmanns: ")
                #if employee_ssn_input != "r":
                    empl_info_lst = self.__get_employee.get_employee(employee_ssn_input)
                    if empl_info_lst != False:
                        # print(self.GO_BACK +"\n") 
                        # print("Starfsmaður ekki til! Vitlaus kennitala.")
                        # employee_ssn_input = input("Kennitala starfsmanns: ")
                        # empl_info_lst = self.__get_employee.get_employee(employee_ssn_input)
                        # if employee_ssn_input == "r":
                        #     self.get_menu()  
                        if get_input != "r":
                            info_output = Employee(empl_info_lst)  
                            print(self.BORDER * self.WITDH +"\n" + int((self.WITDH - len("Sækja starfsmann"))/2)*" " +  "Sækja starfsmanni"  +   "\n" + self.BORDER * self.WITDH )
                            print(self.PICK +"\n")
                            print(self.GO_BACK +"\n")  
                            print("Kennitala: {}".format(info_output.get_ssn()))        
                            print("Nafn: {}".format(info_output.get_name())) 
                            print("Starfsheiti: {}".format(info_output.get_role()))
                            print("Stöðugildi: {}".format(info_output.get_rank()))
                            print("Leyfi: {}".format(info_output.get_licence()))
                            print("Heimilisfang: {}".format(info_output.get_address()))
                            print("Símanúmer: {}".format(info_output.get_phone()))
                            print()
                            get_input = input(self.USER_INPUT)
                        else:
                            self.employee_menu()
                    else:
                        if employee_ssn_input == "r":
                            self.employee_menu()  
                        print()    
                        print("Starfsmaður ekki til! Vitlaus kennitala.")
                        print()
                # else:
                #     self.employee_menu()

            # if get_input =="r":
            #     self.get_menu()
                  