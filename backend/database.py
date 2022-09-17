from firebase_admin import credentials, firestore, initialize_app
from google.cloud import firestore as f_store

from utils import hash_pin

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
        hashed_pin = hash_pin(pin)
        user_data = {
            "name": name,
            "id": id,
            "pin": hashed_pin
        }
        user = User.query_user_document(phone_num)
        user_obj = user.get()
        if user_obj.to_dict() is None:
            user.set(user_data)

    @staticmethod
    def get(phone_num):
        user = User.query_user_document(phone_num).get()
        if user:
            return user.to_dict()
        else:
            return None

    @staticmethod
    def change_pin(phone_num, new_pin):
        queried_user = User.query_user_document(phone_num)
        if queried_user:
            new_pin_hash = hash_pin(new_pin)
            queried_user.update({"pin": new_pin_hash})
            return True
        return False

    @staticmethod

    def transfer(sender,reciever, balance):
        pass
    def transfer(sender_num, receiver_num, balance):
        sender = User.query_user_document(sender_num)
        receiver = User.query_user_document(receiver_num)
        if sender and receiver:
            sender_dict = sender.get().to_dict()
            if sender_dict["balance"] >= balance:
                sender.update({u"balance": balance})
                receiver.update({u"balance": f_store.Increment(balance)})

    @staticmethod
    def get_balance(phone_num):
        user = User.query_user_document(phone_num)
        return user['phone_num'] if user else None

    @staticmethod
    def delete(phone_num):
        pass

    @staticmethod
    def get_pin(phone_num):
        user = User.get(phone_num)
        if user:
            return user.get("pin", None)
        return None

    @staticmethod
    def verify_pin(hashed_pin, pin):
        if hash_pin(pin) == hashed_pin:
            return True
        return False


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
