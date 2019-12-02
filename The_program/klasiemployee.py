class Starfsmadur:

    def __init__(self, empl_info_list):
        self.stm_dict = {}
        self.empl_info_list = empl_info_list
        self.nafn = self.empl_info_list[0]
        self.kennitala = self.empl_info_list[1]
        self.heimilisfang = self.empl_info_list[2]
        self.heimasimi = self.empl_info_list[3]
        self.gsmsimi = self.empl_info_list[4]
        self.netfang = self.empl_info_list[5]
        self.val = self.empl_info_list[1:6]
        self.stm_dict[self.nafn] = self.val      
  
    def __str__(self):
        prnt_str = ""
        prnt_str += self.nafn + "\n"
        for i in self.val:
            prnt_str += i + "\n"
            #if self.val.index(i) < (len(self.val)-1):
            #    prnt_str += "\n"
        return prnt_str

