import requests
import json
import os
from app.utils.utilmes import TextPresentacion, ObteniendoDatosdeusuario, listaMenu, ConfirmarPedido, Pedido, Direccion



def SendMessageWhatsapp(data):
    try:
        token = os.getenv("TOKEN")
        api_url= os.getenv("API_URL")
        print(api_url)
        headers = {"Content-Type": "application/json", "Authorization":f"Bearer {token}"}
        response = requests.post(api_url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            return True
        return False
    except Exception as e:
        print(e)
        return False

def GenerateMessage(messageUser, number):
    data = None
    messagenormal =messageUser
    messageUser = messageUser.lower()
    if "hola" in messageUser or "buenas" == messageUser:
        data = TextPresentacion(number)
    elif "1)" in messageUser:
        data = ObteniendoDatosdeusuario(messageUser, number)
    elif "menu" == messageUser:
        data = listaMenu(number)     
    elif "direccion" in messageUser:
        data = Direccion(messageUser, number)
    elif "si" == messageUser:
        data = ConfirmarPedido(messageUser, number)
    
    else:
        data = Pedido(messagenormal, number) 

    return data
