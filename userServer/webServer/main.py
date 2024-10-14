import flask

app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("home.html")

@app.route("/turnon", methods=["POST"])
def turnOn():
    print("Led turned on")
    return flask.render_template("home.html")
   

@app.route("/turnoff", methods=["POST"])
def turnOff():
    print("Led turned off")
    return flask.render_template("home.html")


if __name__ == "__main__":
    print("Launching web server...")
    app.run(host="0.0.0.0", port=80)
