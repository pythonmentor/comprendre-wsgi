import flask

app = flask.Flask(__name__)


@app.route("/hello/")
def hello():
    return "Bonjour à tous"
