from app import api
from flask_restx import Resource
from flask import request
from app.controllers.webhookWhatsapp_controller import Webhook
import flask_cors

webhook_ns = api.namespace (
    name = "Webhook",
    description ="Ruta para la verificacion y recibir mensajes",
    path="/whatsapp"
)


@webhook_ns.route("")
class Whatsapp(Resource):
    def get(self):
        query = request
        controller = Webhook()
        return controller.VerifyToken(query=query)
    def post(self):
        query = request
        controller = Webhook()
        return controller.ReceiverMessage(query=query)


