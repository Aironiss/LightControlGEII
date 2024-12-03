import json
from json.decoder import JSONDecodeError
from api.light.Light import Light
import os

class LightManager():
    def __init__(self):
        self.lights = []
        with open(file="api/resources/Lights.json", mode="r") as existingLightsFile:
            try:
                jsonParsed = json.load(existingLightsFile)
                for jsonLight in jsonParsed["Lamps"]:
                    print(jsonLight)
                    self.lights.append(Light(pin=int(jsonLight["Pin"]), id=jsonLight["Id"], name=jsonLight["Name"], state=jsonLight["State"]))
            except JSONDecodeError:
                pass

    def refreshLightsFile(self):
        isFile = os.path.isfile("api/resources/Lights.json")
        content = {"Lamps": []}
        with open("api/resources/Lights.json", "w") as newFile:
            try:
                json.dump(content, newFile)
            except Exception as e: print(e)

        with open("api/resources/Lights.json", "r") as readedNewFile:
            try:
                jsonParsed = json.load(readedNewFile)
            except Exception as e: print(e)

            for light in self.getLights():
                jsonParsed["Lamps"].append(light.get_info())

        with open("api/resources/Lights.json", "w") as modifiedNewFile:
            try:
                json.dump(jsonParsed, modifiedNewFile)
            
            except Exception as e: print(e)        

    def getLights(self):
        lights = []
        for light in self.lights:
            lights.append(light)
        return lights
    
    def getLightsId(self):
        ids = []
        for light in self.lights:
            ids.append(light.getId())
        return ids
    
    def getInfoById(self, id, info="State"):
        for light in self.lights:
            if light.get_id() == id:
                if info == "State":
                    return light.get_state()
                elif info == "Name":
                    return light.get_name()
                else : 
                    return light.get_info()
            
    def addLight(self, light):
        print(f"Light {light.get_name()} added to manager")
        jsonParsed = None

        with open(file="api/resources/Lights.json", mode="r") as readExistingLightsFile :
            try:
                jsonParsed = json.load(readExistingLightsFile)
            except Exception as e: print(e)

        print(jsonParsed)
        jsonParsed["Lamps"].append(light.get_info())
        print(jsonParsed)
        
        with open(file="api/resources/Lights.json", mode="w") as writeExistingLightsFile :
            try:
                json.dump(jsonParsed, writeExistingLightsFile)
            except Exception as e: print(e)

        return light.get_info()
    
    def changeLightState(self, lightId, action):
        with open(file="api/resources/Lights.json", mode="r") as readExistingLightsFile :
            try:
                jsonParsed = json.load(readExistingLightsFile)
            except Exception as e: print(e)
        
        changedLightPos = None
        for i in range(len(self.lamps)):
            if self.lamps[i] == lightId:
                changedLightPos = i
                break

        for i in range(len(jsonParsed["Lamps"])):
            if jsonParsed["Lamps"][i]["Id"] == lightId:
                if action == "turnOn":
                    self.lamps[changedLightPos].turnOn()
                    jsonParsed["Lamps"][i]["State"] = "on"
                elif action == "turnOff":
                    self.lamps[changedLightPos].turnOff()
                    jsonParsed["Lamps"][i]["State"] = "off"
                changedJsonLight = jsonParsed["Lamps"][i]
                break

        #for lamp in self.lamps:
        #    if lamp.id == 

        with open(file="api/resources/Lights.json", mode="w") as writeExistingLightsFile :
            try:
                json.dump(jsonParsed, writeExistingLightsFile)
            except Exception as e: print(e)

        print(changedLight)
        return changedLight
    
    def removeLight(self, lightId):
        print("rmLight called from Manager")
        with open(file="api/resources/Lights.json", mode="r") as readExistingLightsFile :
            try :
                jsonParsed = json.load(readExistingLightsFile)
            except Exception as e: print(e)
        
        i = 0
        for light in jsonParsed["Lamps"]:
            if light["Id"] == lightId:
                lightToRm = light
            else:
                i+=1
            
            jsonParsed["Lamps"].pop(i)
        
        with open(file="api/resources/Lights.json", mode="w") as writeExistingLightsFile :
            try:
                json.dump(jsonParsed, writeExistingLightsFile)
            except Exception as e: print(e)

        print(lightToRm)
        return lightToRm
