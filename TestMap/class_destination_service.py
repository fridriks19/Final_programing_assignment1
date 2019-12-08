from class_DestinationRepo import DestinationRepo

class Destination_service():
    def __init__(self):
        self.__destination_repo = DestinationRepo()

    def add_destination(self, dest_str= ""):
        self.dest_str = dest_str
        if self.is_dest_valid(self.dest_str):
            return self.__destination_repo.add_dest(self.dest_str)

    def get_dest(self, user_input): 
        self.user_input = user_input
        if self.is_dest_valid(self.user_input):
            return self.__destination_repo.get_dest_change(self.user_input)

    def get_alldest(self):
        return self.__destination_repo.get_alldest()

    def change_dest(self, choice, change, dest):
        self.choice = choice
        self.change = change
        self.dest = dest
        if self.is_dest_valid_change(self.choice, self.change):
            destination_change = self.__destination_repo.change_dest(self.choice, self.change, self.dest)
            return destination_change

    def is_dest_valid(self, user_input):
        #safas
        return True

    def is_dest_valid_change(self, choice, change):
        return True