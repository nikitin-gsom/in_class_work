from flask import Flask

app = Flask(__name__)


@app.route("/moderator")
def hello_user():
    return "Hello moderator"


if __name__ == "__main__":
    app.run(debug=False)

