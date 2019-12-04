
class Employee:

    def __init__(self, empl_info_list):
        #self.stm_dict = {}
        self.empl_info_list = empl_info_list
        self.kennitala = self.empl_info_list[0]
        self.nafn = self.empl_info_list[1]
        self.starfsheiti = self.empl_info_list[2]
        self.stodugildi = self.empl_info_list[3]
        self.rettindi = self.empl_info_list[4]
        self.heimilisfang = self.empl_info_list[5]
        self.gsmsimi = self.empl_info_list[6]
        self.val = self.empl_info_list[0:7]
        #self.val.pop(1)
        #self.stm_dict[self.nafn] = self.val      
  
    def __str__(self):
        #return "{}".format(self.stm_dict)
        return "{}".format(self.empl_info_list)
    
    def get_name(self):
        return self.nafn
    
    def get_role(self):
        return self.starfsheiti

    def get_ssn(self):
        return self.kennitala

