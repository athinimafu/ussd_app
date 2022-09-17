import os

from dotenv import load_dotenv
from flask import Flask
from flask import request
import africastalking

load_dotenv()

AT_SANDBOX = os.environ.get("AT_SANDBOX")
AT_KEY = os.environ.get("AT_KEY")
africastalking.initialize(AT_SANDBOX, AT_KEY)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "hello world"


@app.route('/callback', methods=["GET", "POST"])
def callback():
    response = ""
    print(request.values)
    response += "CON Hello World"
    return response


if __name__ == '__main__':
    app.run(debug=True, port=5000)
