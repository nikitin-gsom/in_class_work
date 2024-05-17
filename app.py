from flask import Flask

app = Flask(__name__)


@app.route("/user")
def hello_user():
    return "Hello user"


if __name__ == "__main__":
    app.run(debug=False)

