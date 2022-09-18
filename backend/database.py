from datetime import datetime

from firebase_admin import credentials, firestore, initialize_app
from google.cloud import firestore as f_store
from google.cloud.firestore_v1 import DocumentReference

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
    def query_user_document(phone_num) -> DocumentReference:
        return users.document(phone_num)

    @staticmethod
    def create(phone_num, name, id, pin):
        hashed_pin = hash_pin(pin)
        user_data = {
            "name": name,
            "id": id,
            "pin": hashed_pin,
            "balance": 0
        }
        user = User.query_user_document(phone_num)
        if not user.get().exists:
            user.set(user_data)

    @staticmethod
    def get(phone_num):
        user = User.query_user_document(phone_num).get()
        if user.exists:
            return user.to_dict()
        else:
            return None

    @staticmethod
    def change_pin(phone_num, new_pin):
        queried_user = User.query_user_document(phone_num)
        if queried_user.get().exists:
            new_pin_hash = hash_pin(new_pin)
            queried_user.update({"pin": new_pin_hash})
            return True
        return False

    @staticmethod
    def transfer(sender_num, receiver_num, amount):
        sender = User.query_user_document(sender_num)
        receiver = User.query_user_document(receiver_num)
        if sender.get().exists and receiver.get().exists:
            sender_dict = sender.get().to_dict()
            if sender_dict["balance"] >= amount:
                sender.update({u"balance": f_store.Increment(-amount)})
                receiver.update({u"balance": f_store.Increment(amount)})
                Transaction.create(sender, receiver, amount)

    @staticmethod
    def get_balance(phone_num):
        user = User.query_user_document(phone_num)
        if user.get().exists:
            return user.get().to_dict()['balance']
        else:
            return None

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

    @staticmethod
    def delete(phone_num):
        user = User.query_user_document(phone_num)
        if user.get().exists:
            user.delete()
            return True
        return False


class Transaction:
    @staticmethod
    def query_transac_document(transac_id) -> DocumentReference:
        return transaction_ref.document(transac_id)

    @staticmethod
    def create(sender: DocumentReference, receiver: DocumentReference, amount):
        transac_data = {
            "amount": amount,
            "sender": sender.id,
            "receiver": receiver.id,
            "date": datetime.utcnow()
        }
        transaction_ref.add(transac_data)

    @staticmethod
    def get(transac_id):
        transac = Transaction.query_transac_document(transac_id)
        if transac.get().exists:
            return transac.get().to_dict()
        return None


class Business(User):

    @staticmethod
    def query_user_document(phone_num) -> DocumentReference:
        return business_ref.document(phone_num)

    @staticmethod
    def get(phone_num):
        business = Business.query_user_document(phone_num)
        if business.get().exists:
            return business.get().to_dict()
        return None

    # @staticmethod
    # def deposit(receiver_num, amount):
    #     receiver = User.query_user_document(receiver_num)
    #     if receiver.get().exists:
    #         receiver_dict = receiver.get().to_dict()
    #         if receiver_dict["balance"] >= amount:
    #             receiver.update({u"balance": f_store.Increment(-amount)})
    #             receiver.update({u"balance": f_store.Increment(amount)})
    #             Transaction.create(sender, receiver, amount)
