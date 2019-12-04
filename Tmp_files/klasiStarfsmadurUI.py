class StarfsmadurUI:

    def __init__(self, empl_str):
        self.empl_str = empl_str
        self.empl_list = self.empl_str.split(",")
        self.name = self.empl_list[1]
        self.empl_dict = {}
        self.val = self.empl_list
        self.val.pop(1)
        self.empl_dict[self.name] = self.val

    def __str__(self):
        return self.empl_str
        #return "{}".format(self.empl_dict)

    def show_starfsmadur(self):
        return self.empl_dict

st_ui = StarfsmadurUI("9653,dfgh,Pilot,jhgfd,jhgfds,ghg,66")

