from flask_restx import fields
from flask_restx.reqparse import RequestParser
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.fields import Nested
from app.models.menu_model import Menu

class MenuRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=5, location='args')
        return parser

    def create(self):
        return self.namespace.model('Menu Create', {
            'name': fields.String(required=True, max_length=120),
            "precio": fields.Integer(required=True),
            "detalle": fields.String(required=True, max_length=250),
            "categoria_id": fields.Integer(required=True)
        })
    
    
    def update(self):
        return self.namespace.model('Menu Update', {
            'detalle': fields.String(required=False, max_length=120),
            "precio": fields.Integer(required=True),
            'stock': fields.Integer(required=True),
        })
    

class MenuResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Menu
        ordered = True
        #exclude = ['password']