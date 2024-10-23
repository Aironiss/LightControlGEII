import flask
import json
import random
from api.light.LightManager import LightManager
from api.light.Light import Light

blueprint = flask.Blueprint("api", __name__, template_folder="templates")

@blueprint.route('/lamps', methods=["GET"])
def getLamps():
	lightManager = LightManager()
	print("getLamps called.")
	return [existingLight.get_info() for existingLight in lightManager.getLights()]
	
@blueprint.route('/lamps/<id>', methods=["PUT"])
def changeState(id):
	lightManager = LightManager()
	#print(flask.request.get_json())
	datas = str(flask.request.get_data())
	if "turnOn" in datas :
		changedLight = lightManager.changeLightState(lightId=id, action="turnOn")
		print(changedLight)
		return changedLight
	elif "turnOff" in datas :
		return "Turn off"
	else :
		return "Error : No valid action found !"
	#action = flask.request.get_json()
	#print(f"chageState called for {id} with value {action}.")
	

@blueprint.route('/add/<lightName>')
def add(lightName):
	lightManager = LightManager()
	print("Add Light called.")
	for existingLight in lightManager.getLights():
		if lightName == existingLight.get_name():
			print(f"Error : {lightName} is already token by another light.")
			break
	
	light = Light(name=lightName)
	lightManager.addLight(light=light)
	return light.get_info()

@blueprint.route('/state/<lightName>')
def getState():
	print("getState called")
	return 0


@blueprint.route('/turn-on')
def setStateOn(light):
	print("setStateOn called")
	return 0


@blueprint.route('/turn-off')
def setStateOff():
	print("setStateOff called")
	return 0
