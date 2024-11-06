from uuid import uuid1

class Light():
    def __init__(self, id=None, name=id, state="off"):
        self.state = state
        self.name = name
        if id==None:
            self.id = uuid1()
        else : self.id = id

    def get_state(self):
        return self.state
    
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
        self.state = "on"
        return self.get_state()
    
    def turnOff(self):
        self.state = "off"
        return self.get_state()