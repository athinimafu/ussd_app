from firebase_admin import credentials, firestore, initialize_app

# import pyrebase

cred = credentials.Certificate('firebase-key.json')
default_app = initialize_app(cred)
db = firestore.client()
users = db.collection('users')
business_ref = db.collection('businesses')
transaction_ref = db.collection('transactions')


class User:

    @staticmethod
    def query_user_document(phone_num):
        return users.document(phone_num)
    
    @staticmethod
    def create(phone_num, name, id, pin):
        pass

    @staticmethod
    def get(phone_num):
        user = User.query_user_document(phone_num).get()
        if user:
            print(user.to_dict())
            return user.to_dict()
        else:
            return None

    @staticmethod
    def change_pin():
        pass

    @staticmethod

    def transfer(sender,reciever, balance):
        pass
    def transfer(phone_num, balance):
        
        user = User.query_user_document(phone_num)
        # print(user_stream)
        if user:
            print()
            print("before")
            
            # print(user.balance)
            # user.update("phone_num",{u"balance": balance})
            user.update({u"balance": balance})
            
            print("After")
            # print(user.balance)
            # print(user["phone_num"])
        # pass
        return 

    @staticmethod
    def get_balance(phone_num):
        user = User.query_user_document(phone_num)
        return user['phone_num'] if user else None

    @staticmethod
    def delete(phone_num):
        pass


class Transaction:
    @staticmethod
    def get(transac_id):
        pass


class Business(User):
    @staticmethod
    def get(phone_num):
        business = User.get(phone_num)
        if business:
            return business.to_dict()
        return None

    @staticmethod
    def deposit(recipient, amount):
        user = User.get(recipient)
        if user:
            user.update({u"balance":user["amount"]+amount})
        return
