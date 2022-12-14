from httplib2 import Response
from dotenv import load_dotenv
from flask import Flask
from flask import request

from database import Transaction, User

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "hello world"


@app.route('/callback', methods=["GET", "POST"])
def callback():
    user_phone_number = request.values.get("phoneNumber")
    session_code = request.values.get("sessionCode")
    serviceId = request.values.get("serviceCode")
    text = request.values.get("text")
    # query database to see if user is registered if not we call registration code.
    registered = False
    response = ""
    name = "*"

    if text == "":
        response += "CON welcome to cash money \n"
        response += "1. login\n"
        response += "2. register\n"
        response += "3. exit"
        return response
    if text == '1':
        response = ""
        response += "CON enter pin"
        return response

    text_array = text.split("*")
    if text_array[0] == "1":
        user_pin = text_array[1]
        user = User.get(user_phone_number)
        if user:
            if User.verify_pin(user["pin"], user_pin):
                # TODO SET SESSION
                return handle_logged_in_user(request, user_phone_number)
            else:
                return "END Incorrect pin."
        else:
            return "END Account does not exist. Please register first."
    if text_array[0] == "2":
        return handle_reg(request, user_phone_number)
    return "END Invalid option selected"


def handle_logged_in_user(request, phone_num):
    text_array = request.values.get('text').split('*')
    if len(text_array) == 2:
        response = ""
        response += "CON 1. send money\n"
        response += "2. view balance\n"
        return response
    if text_array[0] == "1" and text_array[2] == "1" and len(text_array) >= 3:
        return handle_money_send(request, phone_num)
    if text_array[0] == "1" and text_array[2] == "2" and len(text_array) == 3:
        response = ""
        user = User.get(phone_num)
        user_balance = user["balance"]
        response += f"END Your balance is R{user_balance}"
        return response


def handle_money_send(request, sender_phone_num):
    text_array = request.values.get('text').split('*')
    if text_array[0] == "1" and text_array[2] == "1" and len(text_array) == 3:
        response = ""
        response += "CON Enter recipient's phone number"
        return response
    if text_array[0] == "1" and len(text_array) == 4:
        response = ""
        response += "CON Enter amount"
        return response
    if text_array[0] == "1" and len(text_array) == 5:
        response = ""
        recipient_phone = text_array[3]
        amount = int(text_array[4])
        user = User.get(sender_phone_num)
        if user:
            if int(user["balance"]) >= amount:
                User.transfer(sender_phone_num, recipient_phone, amount)
                response += "END money sent"
            else:
                response += "END Insufficient funds"
        return response


def handle_reg(request, phone_num):
    text_array = request.values.get("text").split('*')
    if len(text_array) == 1:
        response = ""
        response += "CON Enter Name\n"
        return response
    if len(text_array) == 2:
        response = ""
        response += "CON Enter Govid\n"
        return response
    if len(text_array) == 3:
        response = ""
        response += "CON Enter Pin\n"
        return response
    if len(text_array) == 4:
        response = ""
        response += "CON Reenter Pin\n"
        return response
    if len(text_array) == 5:
        uname = text_array[1]
        rsaid = text_array[2]
        pin = text_array[3]
        confirm_pin = text_array[4]

        if pin != confirm_pin:
            return "END Pin does not match"

        User.create(phone_num, name=uname, id=rsaid, pin=pin)
        response = ""
        response += "END Fully registered\n"
        return response


if __name__ == '__main__':
    app.run(debug=True, port=5000)
