
class VoyageRepo():
    
    def __init__(self, voyage_str=""):
        self.voyage_str = voyage_str
    
    def add_voyage(self, new_voyage):
        self.new_voyage = new_voyage
        open_file = open("./data/voyage.csv", "a")
        open_file.write(self.new_voyage + "\n")
        open_file.close()
        return "Vinnuferð vistuð"
    
    def get_voyage(self):
        voyage_list = []
        open_file = open("./data/voyage.csv", "r")
        for line in open_file:
            line = line.strip()
            line = line.split(",")
            voyage_list.append(line)
        open_file.close()
        return voyage_list
