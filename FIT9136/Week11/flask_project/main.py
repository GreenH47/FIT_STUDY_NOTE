from flask import Flask, request,render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    req = request.values
    username = req["username"]
    password = req["password"]
    print(username)
    print(password)
    return "Login success"


@app.route("/register")
def register():
    return "register success"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
