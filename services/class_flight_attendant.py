from models.class_employee import Employee

class flight_attendant(Employee):
    def __init__(self, empl_info_list):
        Employee.__init__(self, empl_info_list)
        self.empl_info_list[2] = "Cabincrew"
        self.empl_info_list[4] = "N/A"

    def __str__(self):
        prnt_str = ""
        prnt_str += self.kennitala + ","
        prnt_str += self.nafn + ","
        for i in self.empl_info_list[2:7]:
            if self.empl_info_list.index(i) == 6:
                prnt_str += i
            else:
                prnt_str += i + ","
        return prnt_str
