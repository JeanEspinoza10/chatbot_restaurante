from app import db
from flask_jwt_extended import current_user
from app.models.users_model import UserModel
import os
from app.utils.whatsappservice import GenerateMessage, SendMessageWhatsapp
from app.utils.utilmes import GetTextUser

from flask import request


# Iniciando las variables



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
            #Obtener el texto y el numero telefonico
            body = request.get_json()
            entry = (body["entry"])[0]
            changes = (entry["changes"])[0]
            value = (changes["value"])
            message = (value["messages"])[0]
            number = message["from"]
            text = GetTextUser(message)

            # Generando la data para enviar
            data = GenerateMessage(text, number)
            

            #Enviando mensaje a whatsapp
            e = SendMessageWhatsapp(data)
            print(e)
            return "EVENT_RECEIVED", data
        except Exception as e:
            print("Error 1", e)
            return "EVENT_RECEIVED"



    