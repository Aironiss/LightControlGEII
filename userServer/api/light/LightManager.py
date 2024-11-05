import json
from json.decoder import JSONDecodeError
from api.light.Light import Light

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
    
    def getLightById(self, id):
        for light in self.lights:
            if light.getId() == id:
                return light
            
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

        print(changedJsonLight)
        return changedJsonLight
