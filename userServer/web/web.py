import flask

blueprint = flask.Blueprint("web", __name__, template_folder="templates", static_folder="static", static_url_path="/web/static")

@blueprint.route("/")
def home():
    return flask.render_template("home.html")

@blueprint.route("/turnon", methods=["POST"])
def turnOn():
    print("Led turned on")
    return flask.render_template("home.html")
   

@blueprint.route("/turnoff", methods=["POST"])
def turnOff():
    print("Led turned off")
    return flask.render_template("home.html")