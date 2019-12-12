from repo.class_DestinationRepo import DestinationRepo

class Destination_service():
    def __init__(self):
        self.__destination_repo = DestinationRepo()

    def add_destination(self, dest_str= ""):
        '''Sends the destination string to the Destination Repository'''
        self.dest_str = dest_str
        if self.is_dest_valid(self.dest_str):
            return self.__destination_repo.add_dest(self.dest_str)
        else:
            return "Upplýsingar ekki gildar"

    def get_dest(self, user_input): 
        '''Gets a destination matching the user input from the repository'''
        self.user_input = user_input
        return self.__destination_repo.get_dest(self.user_input)

    def get_alldest(self):
        '''Gets all destinations in a formatted string'''
        return self.__destination_repo.get_alldest()

    def change_dest(self, choice, change, dest):
        '''Sends changes to the repository where it gets written to file'''
        self.choice = choice
        self.change = change
        self.dest = dest
        if self.is_dest_valid_change(self.choice, self.change):
            destination_change = self.__destination_repo.change_dest(self.choice, self.change, self.dest)
            return destination_change
    
    def get_all_dest_list(self):
        '''Gets a list with all destinations'''
        return self.__destination_repo.get_all_dest_list()


    def is_dest_valid(self, user_input):
        '''Checks if the created destination includes a digit'''
        self.user_input = user_input
        user_input_list = self.user_input.split(",")
        for letter in user_input_list[0]:
            if letter.isdigit():
                return False
        for letter in user_input_list[1]:
            if letter.isdigit():
                return False
        return True

    def is_dest_valid_change(self, choice, change):
        '''Allan please add detail'''
        return True