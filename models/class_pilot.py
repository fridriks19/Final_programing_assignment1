from models.class_employee import Employee

class pilot(Employee):
    ''' Sets the role for pilots as "Pilot" '''
    def __init__(self, empl_info_list):
        Employee.__init__(self, empl_info_list)
        self.empl_info_list[2] = "Pilot"

    def __str__(self):
        prnt_str = ""
        for i in self.empl_info_list[0:7]:
            if self.empl_info_list.index(i) == 6:
                prnt_str += i
            else:
                prnt_str += i + ","
        return prnt_str