import flask
import json
import random

blueprint = flask.Blueprint("api", __name__, template_folder=template)

@blueprint.route('/state')
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
