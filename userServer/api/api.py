import flask
import json
import random
from api.Light import Light

blueprint = flask.Blueprint("api", __name__, template_folder="templates")

@blueprint.route('/add/<lightName>')
def add(lightName):
	print("add called")

	light = Light(lightName)
	print(f"Light {light.get_name()} created")

	with open(file="resources/Lights.json", mode="r+") as existingLightsFile:

		existingLights = json.load(existingLightsFile)

		for existingLight in existingLights :
			if existingLight["Name"] == lightName:
				print(f"Error : Light has same name as {lightName}")
				break
		
		json.dump(light.get_info(), existingLightsFile)
	
	existingLightsFile.close()

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
