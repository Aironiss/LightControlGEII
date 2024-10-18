import flask
import web.web
import api.api

app = flask.Flask(__name__)

app.register_blueprint(blueprint=api.api.blueprint, url_prefix="/api")
app.register_blueprint(blueprint=web.web.blueprint, url_prefix="/")

if __name__ == "__main__":
    print("Launching web server...")
    app.run(host="0.0.0.0", port=80)
