from dotenv import load_dotenv
from flask import Flask
from flask import request

from database import Transaction, User, users

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "hello world"


@app.route('/callback', methods=["GET", "POST"])
def callback():
    User.delete("0660277901")
    Transaction.get("0H3pzryAVNct0nbFfn68")
    user_phone_number = request.values.get("phoneNumber")
    session_code = request.values.get("sessionCode")
    serviceId = request.values.get("serviceCode")
    text = request.values.get("text")
    # query database to see if user is registered if not we call registration code.
    registered = False
    response = ""
    print(request.values)
    response += "CON Hello World"
    return response


if __name__ == '__main__':
    app.run(debug=True, port=5000)
