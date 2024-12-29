import uuid
import pigpio


class Button():
    def __init__(self, pin, id=None, name=id, light=None):
        self.pin = pin #Pin number of the GPIO
        self.id = str("btn_" + uuid.uuid1()) #ID to identify the gpio in the application
        self.name = name #Name to help user to identify the GPIO
        self.light = light
        #GPIO configuration
        pigpio.pi().set_mode(self.pin, pigpio.INPUT) #Setting the gpio as an INPUT
        pigpio.pi().set_pull_up_down(self.pin, pigpio.PUD_DOWN) #Setting a PULL DOWN resistor for the GPIO
        if self.light == None:
            print(f"The {self.name} button doesn't have any assigned light.")
        if self.name == self.id :
            print(f"The {self.id} button doesn't have any name.")

    def getInfos(self):
        outDict = {
            "pin" : self.pin,
            "id" : self.id,
            "name" : self.name
        }
        return outDict
    
    
    
    