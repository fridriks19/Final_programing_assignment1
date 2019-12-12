import datetime
from repo.class_FlightRepository import FlightRepository
from repo.class_voyageRepo import VoyageRepo
from repo.class_EmployeeRepository import EmployeeRepository

class Worktime_service:

    def __init__(self, work_date):
        self.work_date = work_date
        self.work_date = self.work_date.split("T")
        self.work_date = self.work_date[0]
        self.flight_list = FlightRepository().get_upcomingflights()
        self.crew_list = EmployeeRepository().get_allemployees_list()
    
    def is_working_list(self):
        empl_list = []
        for flight in self.flight_list[1:]:
            flight[3] = flight[3].split("T")
            if flight[3][0] == self.work_date:
                for employee in flight[6:]:
                    if employee not in empl_list:
                        empl_list.append(employee)
        return empl_list
    
    def not_working_list(self):
        not_working_list = []
        work_crew = Worktime_service(self.work_date).is_working_list()
        for employee in self.crew_list:
            if employee[0] not in work_crew:
                not_working_list.append(employee)
        return not_working_list

    def working_list_destination(self):   # Returns all the employees that are working on a specific date 
        empl_list = []
        empl_and_dest = []
        for flight in self.flight_list[1:]:
            flight[3] = flight[3].split("T")
            if flight[3][0] == self.work_date:
                for employee in flight[6:]:
                    if employee not in empl_list:
                        new_empl = [employee, flight[2]]
                        empl_list.append(new_empl)
        return empl_list

    # def not_working_print(self):
    #     not_working_list = Worktime_service(self.work_date).not_working_list()
    #     prnt_list = []
    #     for empl in not_working_list:
    #         print(empl[0])


