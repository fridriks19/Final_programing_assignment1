
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
        pass
