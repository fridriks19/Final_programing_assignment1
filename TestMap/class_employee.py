
class Employee:

    def __init__(self, empl_info_list):
        #self.stm_dict = {}
        self.empl_info_list = empl_info_list
        self.ssn = self.empl_info_list[0]
        self.name = self.empl_info_list[1]
        self.role = self.empl_info_list[2]
        self.rank = self.empl_info_list[3]
        self.licence = self.empl_info_list[4]
        self.address = self.empl_info_list[5]
        self.phone = self.empl_info_list[6]   
  
    def __str__(self):
        #return "{}".format(self.stm_dict)
        return "{}".format(self.empl_info_list)
    
    def get_ssn(self):
        return self.ssn

    def get_name(self):
        return self.name    

    def get_role(self):
        return self.role
    
    def get_rank(self):
        return self.rank
    
    def get_licence(self):
        return self.licence

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone