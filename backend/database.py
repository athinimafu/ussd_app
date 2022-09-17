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
    def create(phone_num, name, id, pin):
        pass

    @staticmethod
    def get(phone_num):
        user_stream = users.where(u"phone_num", u"==", f'u{phone_num}').stream()
        if len(user_stream) > 0:
            return user_stream[0]
        return None

    @staticmethod
    def change_pin():
        pass

    @staticmethod
    def transfer(phone_num, balance):
        pass

    @staticmethod
    def get_balance(phone_num):
        pass

    @staticmethod
    def delete(phone_num):
        pass


class Transaction:
    @staticmethod
    def get(transac_id):
        pass


class Business(User):
    @staticmethod
    def deposit(recipient, amount):
        pass
