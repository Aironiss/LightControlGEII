from uuid import uuid1

class Light():
    def __init__(self, id=uuid1(), name=id):
        self.turnedOn = False
        self.id = id
        self.name = name

    def get_state(self):
        return self.turnedOn
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_info(self):
        infos = {
            "State" : str(self.get_state()),
            "Id" : str(self.get_id()),
            "Name" : str(self.get_name())
            }
        return infos
    
    def turnOn(self):
        self.turnedOn = True
        return self.get_state()
    
    def turnOff(self):
        self.turnedOn = False
        return self.get_state()