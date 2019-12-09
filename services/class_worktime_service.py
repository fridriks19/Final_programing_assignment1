import datetime
from repo.class_FlightRepository import FlightRepository
from repo.class_voyageRepo import VoyageRepo
from repo.class_EmployeeRepository import EmployeeRepository

class Worktime_service:

    def __init__(self, work_date):
        self.work_date = work_date
        self.voyage_list = VoyageRepo().get_voyage()
        self.crew_list = EmployeeRepository().get_allemployees_list()
    
    def is_working(self):
        empl_list = []
        for flight in self.voyage_list[1:]:
            flight[3] = flight[3].split("T")
            if flight[3][0] == self.work_date:
                for employee in flight[6:]:
                    if employee not in empl_list:
                        empl_list.append(employee)
        prnt_str = ""
        for i in empl_list:
            prnt_str += i+"\n"
        return prnt_str
    
    def not_working(self):
        not_working_list = []
        work_crew = Worktime(self.work_date).is_working()
        for employee in self.crew_list:
            if employee not in work_crew:
                not_working_list.append(employee)
        prnt_str = ""
        for i in not_working_list:
            prnt_str += i+"\n"
        return prnt_str

print(Worktime_service().is_working("2019-12-26T12:27:00"))