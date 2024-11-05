from uuid import uuid1
import pigpio

pi = pigpio.pi()

class Light():
    def __init__(self, pin, id=None, name=id, state="off"):
        self.state = state
        self.name = name
        self.pin = pin
        if id==None:
            self.id = uuid1()
        else:
            self.id = id

        pi.set_mode(self.pin, pigpio.OUTPUT)

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
            "Name" : str(self.get_name()),
            "Pin": str(self.pin)
            }
        return infos
    
    def turnOn(self):
        self.state = "on"
        pi.write(ledPin, True)
        return self.get_state()
    
    def turnOff(self):
        self.state = "off"
        pi.write(ledPin, False)
        return self.get_state()
