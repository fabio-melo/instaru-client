import firebase_admin
from firebase_admin import firestore, credentials

config = {
    "apiKey": "AIzaSyAiyTqTAdKO68QeCEQNylVr6ukxkcZLXOk",
    "authDomain": "autoupd-6c999.firebaseapp.com",
    "databaseURL": "https://autoupd-6c999.firebaseio.com",
    "projectId": "autoupd-6c999",
    "storageBucket": "autoupd-6c999.appspot.com",
    "messagingSenderId": "135527685936"
}

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, options=config)

db = firestore.client()