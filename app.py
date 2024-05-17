from flask import Flask

app = Flask(__name__)


@app.route("/user2")
def hello_user():
    return "Hello user2"


if __name__ == "__main__":
    app.run(debug=False)

