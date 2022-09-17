from firebase_admin import credentials, firestore, initialize_app
# import pyrebase

cred = credentials.Certificate('firebase-key.json')
default_app = initialize_app(cred)
db = firestore.client()
users = db.collection('users')
businesses = db.collection('businesses')
transactions = db.collection('transactions')