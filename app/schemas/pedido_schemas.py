from flask_restx import fields
from flask_restx.reqparse import RequestParser
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.fields import Nested
from app.models.pedido_model import PedidoModel

class PedidoRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace
    
    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=5, location='args')
        return parser

    def create(self):
        return self.namespace.model('Crear pedido', {
            'menu_id': fields.Integer(required=True),
            'user_id': fields.Integer(required=True),
            'direccion': fields.String(required=True, max_length=120),
            'estado': fields.String(required=True, max_length=120)
        })
    def update(self):
        return self.namespace.model("Actualizar pedido", {
            "menu_id": fields.Integer(required=True),
            "user_id": fields.Integer(),
            "direccion":fields.String(required=True, max_length=120),
            "estado":fields.String(default="En proceso")
        })
    



class PedidoResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PedidoModel
        ordered = True
        #exclude = ['password']
    
    menus = Nested("MenuResponseSchema",many=False)
    users = Nested("UsersResponseSchema",exclude = ["role"], many=False)
    
