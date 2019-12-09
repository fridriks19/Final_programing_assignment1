from services.class_worktime_service import Worktime_service
from repo.class_Aircraft_typeRepository import AircraftRepository

class Voyage_crew_service:

    def __init__(self, date , planename):
        self.date = date
        self.planename = AircraftRepository().find_air_id(planename)
        self.date = self.date.split("T")
        self.date.pop(1)
        self.not_working_list = Worktime_service(self.date).not_working_list()

    def get_captain(self):
        capt_list = []
        for employee in self.not_working_list:
            if employee[3] == "Captain" and employee[4] == self.planename:
                capt_list.append(employee)
        return capt_list
    
    def get_copilot(self):
        copilot_list = []
        for employee in self.not_working_list:
            if employee[3] == "Copilot" and employee[4] == self.planename:
                copilot_list.append(employee)
        return copilot_list


    def get_fsm(self):
        fsm_list = []
        for employee in self.not_working_list:
            if employee[3] == "Flight Service Manager":
                fsm_list.append(employee)
        return fsm_list

    def get_fa(self):
        fa_list = []
        for employee in self.not_working_list:
            if employee[3] == "Flight Attendant":
                fa_list.append(employee)
        return fa_list

   