

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
    #TODO: insert into database then return SUCCESS or FAILURE
    return

def user_login(pin):
    #TODO: login to session and check whether pin is valid.
    return