from services.class_worktime_service import Worktime_service
from repo.class_Aircraft_typeRepository import AircraftRepository

class Voyage_crew_service:

    def __init__(self, date , planename):
        self.date = date
        self.planename = AircraftRepository().find_air_id(planename)
        # self.date = self.date.split("T")
        # self.date.pop(1)
        self.not_working_list = Worktime_service(str(self.date)).not_working_list()

    def get_captain(self):
        '''Returns a list with all captains that have a lisence for the selected airplane'''
        capt_list = []
        for employee in self.not_working_list:
            if employee[3] == "Captain" and employee[4] == self.planename:
                capt_list.append(employee)
        return capt_list
    
    def get_copilot(self):
        '''Returns a list with all copilots that have a lisence for the selected airplane'''
        copilot_list = []
        for employee in self.not_working_list:
            if employee[3] == "Copilot" and employee[4] == self.planename:
                copilot_list.append(employee)
        return copilot_list


    def get_fsm(self):
        '''Returns a list of all available Flight Service Managers'''
        fsm_list = []
        for employee in self.not_working_list:
            if employee[3] == "Flight Service Manager":
                fsm_list.append(employee)
        return fsm_list

    def get_fa(self):
        '''Returns a list of all available Flight Attendants'''
        fa_list = []
        for employee in self.not_working_list:
            if employee[3] == "Flight Attendant":
                fa_list.append(employee)
        return fa_list

   