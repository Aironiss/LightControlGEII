import flask

blueprint = flask.Blueprint("web", __name__, template_folder="templates", static_folder="static", static_url_path="/web/static")

@blueprint.route("/")
def home():
    return flask.render_template("home.html")
