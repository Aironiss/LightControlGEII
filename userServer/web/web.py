import flask

blueprint = flask.Blueprint("web", __name__, template_folder="templates", static_folder="static", static_url_path="/web/static")

@blueprint.route("/")
def home():
    return flask.render_template("home.html")

@blueprint.route("/lamps", methods=["GET"])
def getLamps():
    return flask.jsonify([
    {
        "id": 101,
        "name": "Living room 1",
        "state": "off"
    }, {
        "id": 42,
        "name": "Living room 2",
        "state": "on"
    }
])
