import hashlib
from database import users,User

def user_in_db(phone_number):
    #checks wether the user doc is already present in the database.
    users_found = users.where(u"phoneNumber",u"==",u'{phone_number}').stream()
    if len(users_found) == 0:
        return False
    return users_found[0]



def user_registration(properties):

    #properties : [ name, pin, confirmPin, phoneNumber ,ID ]
    if len(properties) == 1:
        return "please insert your full name"
    elif len(properties) == 2:
        return "please insert pin"
    elif len(properties) == 3:
        return "please insert confirmation of pin"
    elif len(properties) == 4:
        return "please insert your id"
    name,_id,pin,confirmPin,phoneNumber = properties
    user = {
        name,
        phoneNumber
    }
    
    user["id"] = _id

    if pin != confirmPin:
        return "pin and confirmation pin doesn't match"

    user["pin"] = hashlib.sha256(pin).digest()

    if user_in_db(phoneNumber):
        return "phone number already registered"
    #TODO: insert into database then return SUCCESS or FAILURE
    users.add(user)
    return


def user_login(phone_number,pin):
    #TODO: login to session and check whether pin is valid.
    user_inst = User()
    user_doc = user_inst.get(phone_number)
    if user_doc:
        
        user_doc = user_doc.to_dict() 
        if user_doc["pin"] == hashlib.sha256(pin).digest():
            return [ 0," login successful! "]
        else: 
            return [ 1," invalid pin! " ]
    return [2," user is not registered! "]


