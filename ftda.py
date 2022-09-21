import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("flask-api-todo-firebase-firebase-adminsdk-whbps-56e8e8ced9.json")
firebase_admin.initialize_app(cred)