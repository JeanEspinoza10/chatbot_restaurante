from app import db
from flask_jwt_extended import current_user
from app.models.users_model import UserModel
import os

class Webhook():
    def __init__(self):
        self.model = UserModel
        self.current_user = current_user

    def VerifyToken(self, query):
        try:
            accessToken = os.getenv("ACCES_TOKEN")
            token = query.args.get("hub.verify_token")
            challenge = query.args.get("hub.challenge")
            if token != None and challenge != None and token == accessToken:
                return challenge
            else:
                return "No se valido correctamente", 400
        except: 
            return"Error", 400
    
    def ReceiverMessage(self, query):
        try:
            body = query.get_json()
            entry = (body["entry"])[0]
            changes = (entry["changes"])[0]
            value = (changes["value"])
            message = (value["messages"])[0]
            messageUser = (message["text"])["body"]
            number = message["from"]
            #text = util.GetTextUser(message)
            #GenerateMessage(messageUser, number)
            print(messageUser)

            return "EVENT_RECEIVED"
        except Exception as e:
            print("Error 1", e)
            return "EVENT_RECEIVED"

    