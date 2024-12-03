import flask
import json
import random

from api.light.LightManager import LightManager
from api.light.Light import Light


blueprint = flask.Blueprint("api", __name__, template_folder="templates")
lightManager = LightManager()


@blueprint.route('/lamps', methods=["GET"])
def getLamps():
	return [existingLight.get_info() for existingLight in lightManager.getLights()]

	
@blueprint.route('/lamps/<id>', methods=["PUT"])
def changeState(id):
	datas = str(flask.request.get_data())
	if "turnOn" in datas :
		changedLight = lightManager.changeLightState(lightId=id, action="turnOn")
		return changedLight
	elif "turnOff" in datas :
		changedLight = lightManager.changeLightState(lightId=id, action="turnOff")
		return changedLight
	else :
		return "Error : No valid action found !"
	

@blueprint.route('/add/<lightName>')
def add(lightName):
	for existingLight in lightManager.getLights():
		if lightName == existingLight.get_name():
			print(f"Error : {lightName} is already token by another light.")
			break
	
	light = Light(name=lightName)
	lightManager.addLight(light=light)
	return light.get_info()


@blueprint.route('/state/<id>')
def getState(id):
	lightManager = LightManager()
	return lightManager.getInfoById(id=id, info="State")


@blueprint.route('/rm/<id>')
def rmLight(id):
	lightManager = LightManager()
	print(id)
	return lightManager.removeLight(id)
	