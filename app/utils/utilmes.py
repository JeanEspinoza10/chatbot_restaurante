from app.controllers.users_controller import UserController
from app.models.users_model import UserModel
from app.models.menu_model import Menu
from app.models.pedido_model import PedidoModel
import datetime
from app import db
from app.schemas.menu_schemas import MenuResponseSchema

# Identificar el mensaje del usuario #


def GetTextUser(message):
    text = ""
    typeMessage = message["type"]
    if typeMessage == "text":
        text = (message["text"])["body"]
        

    elif typeMessage == "interactive":
        interactiveObject = message["interactive"]
        typeInteractive = interactiveObject["type"]
        if typeInteractive == "button_reply":
            text = (interactiveObject["button_reply"])["title"]
        elif typeInteractive == "list_reply":
            text = (interactiveObject["list_reply"])["title"]
        else:
            print("sin mensaje")
    else:
        print("sin mensaje")
    
    return text



def TextPresentacion(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": "Hola, buenas tardes. Puede brindarnos los siguientes datos: 1) Nombre y apellidos 2) Correo"
                }
        }
    
    return data



def TextFormatMessage(text, number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": f"{text}"
                }
        }
    return data




def listaMenu(number):
    try:
        # Obtener los datos de la base de datos y enviarlo mediante whatsapp.
        resultadoDic = []
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        resultados = db.session.query(Menu).filter_by(fecha=current_date, disonibilidad=True).order_by(Menu.id)
        for resultado in resultados:
            dic = {
                "id": resultado.id,
                "title": resultado.name,
                "description":resultado.detalle
            }
            resultadoDic.append(dic)
    
        data =  {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "body": {
                    "text": "Nuestra Carta"
                },
                "footer": {
                    "text": "Escoger una opcion"
                },
                "action": {
                    "button": "Ver",
                    "sections": [
                        {
                            "title": "Platos",
                            "rows": resultadoDic
                        }
                    ]
                }
            }
        }

    
        return data
    except Exception as e:
        print(e)

    

def ObteniendoDatosdeusuario(text, number):
    try:
        
        cadena = text
        hora = datetime.datetime.now().time().strftime('%H:%M')
        nombre, correo = cadena.split("2)")[0].strip().replace("1)", ""), cadena.split("2)")[1].strip()
        username = f"{nombre}{hora}"
        data = {
                "name": nombre,
                "last_name": nombre,
                "username": username,
                "password": "sindatos",
                "email": correo,
                "rol_id": 2,
                "phone":number
            }
        # Grabando los datos en la base de datos.        
        usuarios = UserModel(**data)
        usuarios.hashPassword()
        db.session.add(usuarios)
        db.session.commit()
             
        respuesta = "Gracias por la inforacion . Por favor, brindarme su direccion anteponiendo la palabra direccion."
        data = TextFormatMessage(respuesta, number)

        return data
    except Exception as e:
        respuesta = "Usted ya tiene registrado su numero de celular. Si desea saber el menu del dia, escribir la palabra Menu"
        data = TextFormatMessage(respuesta, number)
        print(e)
        return data


def Pedido(text, number):
    try:
            # Buscamos el texto en la base de menu si hay menu
        menu = text.splitlines()
        menu = menu[0]
        print(menu)
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        resultados = db.session.query(Menu).filter_by(name=menu, fecha=current_date).order_by(Menu.id)
        menu_id =[]
        for element in resultados:
            menu_id.append(element.id)

        menu = menu_id[0]          
        
           # Buscamos el usuario activo
        usuario_id = 0
        resultados = db.session.query(UserModel).filter_by(phone=number)
        for element in resultados:
            usuario_id = element.id
        print(usuario_id)
        db.session.query(PedidoModel).filter(PedidoModel.menu_id == None, PedidoModel.user_id ==usuario_id).update({PedidoModel.menu_id:menu})
        db.session.commit()



        respuesta = "Desea confirmar su pedido."
        data = TextFormatMessage(respuesta, number)
        return data
    except Exception as e:
        respuesta = "No seleeciono una opcion correcta de nuestro Menu. Por favor, seleeccionar una opcion"
        data = TextFormatMessage(respuesta, number)
        print(e)
        return data


def ConfirmarPedido(text, number):
    try:
        # Creamos el pedido en la base de datos
        respuesta = "Su pedido fue confirmado. En unos momentos, el repartidor se estara comunicando con usted, para coordinar la entrega."
        data = TextFormatMessage(respuesta, number)    
        
    except Exception as e:
        return e
        
    return data
def Direccion(text, number):
    text = text.replace("direccion:", "")
    # Buscamos en la base de datos su numero y colocamos la direccion
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    usuario_id = ""
    resultados = db.session.query(UserModel).filter_by(phone=number)
    for element in resultados:
        usuario_id = element.id
    
    direccion = {
        "estado":"En proceso",
        "fecha": current_date,
        "user_id": usuario_id,
        "direccion":text
    }
    direccion = PedidoModel(**direccion)
    db.session.add(direccion)
    db.session.commit()


    respuesta = "Su direccion fue almacenada. Si desea saber el Menu, digite la palabra Menu"
    data = TextFormatMessage(respuesta, number)
    return data