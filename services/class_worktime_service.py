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

    # def working_list_destination(self):   # Returns all the employees that are working on a specific date 
    #     empl_list = []
    #     empl_and_dest = []
    #     for flight in self.flight_list[1:]:
    #         flight[3] = flight[3].split("T")
    #         if flight[3][0] == self.work_date:
    #             for employee in flight[6:]:
    #                 if employee not in empl_list:
    #                     new_empl = [employee, flight[2]]
    #                     empl_list.append(new_empl)
    #     return empl_list

    def print_working_list_destination(self):
        new_flight_list = []
        for flight in self.flight_list[1:]:
            flight[3] = flight[3].split("T")
            if flight[3][0] == self.work_date:
               new_flight_list.append(flight)
        prnt_str = ""
        staff_list = []
        for flight in new_flight_list:
            for item in flight[6:]:
                if item != "":
                    if item not in staff_list:
                        prnt_str += "Kennitala: {}\tÁfangastaður: {}\n".format(item, flight[2])
                        staff_list.append(item)
        return prnt_str

    def find_empl_worktime(self, ssn, flight_list):
        self.ssn = ssn
        self.flight_list = flight_list
        empl_flight_list = []
        prnt_str = ""
        for flight in flight_list:
            if self.ssn in flight:
                empl_flight_list.append(flight)
        for flight in empl_flight_list:
            flight_time = datetime.datetime.strptime(flight[3], "%Y-%m-%dT%H:%M:%S")
            prnt_str += "Flug: {}\nFrá: {}\nTil: {}\nDags: {}\nFlugstjóri: {}\nAðstoðarflugmaður: {}\nYfirflugþjónn: {}\nFlugþjónn 1: {}\nFlugþjónn 2: {}\n\n".format(flight[0], flight[1], flight[2], flight_time, flight[6], flight [7], flight[8], flight[9], flight[10])
        return prnt_str

        

        

