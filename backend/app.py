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
    User.delete("0660277901")
    Transaction.get("0H3pzryAVNct0nbFfn68")
    user_phone_number = request.values.get("phoneNumber")
    session_code = request.values.get("sessionCode")
    serviceId = request.values.get("serviceCode")
    text = request.values.get("text")
    # query database to see if user is registered if not we call registration code.
    registered = False
    response = ""
    name = "*"
    
    if (text == ""):
        response += "CON welcome to cash money \n"
        response += "1. login\n"
        response += "2. register\n"
        response += "3. exit"
        return response
    text_array = text.split('*')
    if (text == '1'):
        response = ""
        response += "CON enter pin"
        return response
    if request.values.get("text").startswith('1*'):
        
        print(request.values.get("text"))
        return handle_login(request)
    if (request.values.get("text").startswith('2')):
        return handle_reg(request)
    #return response

def handle_login(request):
    text_array = request.values.get('text').split('*')
    if len(text_array) == 2:
        if User.get(text_array[1]):
            response = ""
            response += "CON 1. send money\n"
            response += "2. view balance\n"
            return response
    else:
        response = ""
        response += "END account does not exist please register first\n"
        return response
    if request.values.get("text").endswith('1'):
        print("ends with 1 ==sending money")
        return handle_moneysend(request)
    if request.values.get("text").startswith('1') and  len(text_array) == 4:
        response = ""
        response += "END money sent"
        return response
    text_array = request.values.get('text').split('*')
    print(len(text_array),"length at your balance is")
    if request.values.get("text").endswith('2'):
        response = ""
        response += "END your balance is =="
        return response

def handle_moneysend(request):
    text_array = request.values.get('text').split('*')
    print(len(text_array), "--------")
    if request.values.get("text").startswith('1') and  len(text_array) == 3:
        print("********")
        print(request.values.get("text"))
        response = ""
        response += " CON Enter amount"
        return response
    if request.values.get("text").startswith('1') and  len(text_array) == 4:
        response = ""
        response += "END money sent"
        return response

def handle_reg(request):
    if (request.values.get("text") == '2'):
        response = ""
        response += "CON Enter Name\n"
        return response
    if (request.values.get("text").count('*') == 1):
        print(request.values.get("text"))
        name = ""
        name += request.values.get("text")
        response = ""
        response += "CON Enter Govid\n"
        return response
    if  request.values.get("text").count('*') == 2:
        govid = request.values.get("text")
        print(govid)
        response = ""
        response += "CON Enter Pin\n"
        return response
    if  request.values.get("text").count('*') == 3:
        pin = request.values.get("text")
        response = ""
        response += "CON Reenter Pin\n"
        print(request.values.get("text"))
        return response
    if  request.values.get("text").count('*') == 4:
        user_array = request.values.get('text').split('*')
        uname = user_array[1]
        rsaid = user_array[2]
        pin = user_array[3]
        phone = request.values.get("phoneNumber")
        User.create(phone_num=phone, name=uname, id=rsaid, pin=pin)
        response = ""
        response += "END Fully registered\n"
        print(request.values.get("text"))
        return response
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
