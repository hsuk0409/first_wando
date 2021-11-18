from flask import Flask, request

from web.user.user_handler import UserHandler

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return "hello, wando!"


@app.route("/user", methods=["POST"])
def register_user():
    result = UserHandler(request).register_user()
    return {"result": result}
