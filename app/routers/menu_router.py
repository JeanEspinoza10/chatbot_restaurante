from app import api
from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required
from app.helpers.decorators import role_required
from app.schemas.menu_schemas import MenuRequestSchema
from app.controllers.menu_controller import MenuController
from datetime import datetime



menu_ns = api.namespace(
    name = "Plato de Comida",
    description ="Ruta para los menus",
    path = "/menu"
)

request_schema = MenuRequestSchema(menu_ns)

###############################################
## Ruta para listar menu de hoy y crear menu
###############################################

@menu_ns.route("")
class Menu(Resource):
    @menu_ns.expect(request_schema.all())
    def get(self):
        '''Lista de menu para hoy'''
        query = request_schema.all().parse_args()
        controller = MenuController()
        return controller.all(query)
    
    @menu_ns.doc(security="Bearer")
    @jwt_required()
    @role_required(rol_id=1)
    @menu_ns.expect(request_schema.create(), validate=True)
    def post (self):
        '''Creacion de Menus'''
        controller = MenuController()
        return controller.create(request.json)

@menu_ns.route("/<int:id>")
@menu_ns.doc(security="Bearer")
class MenuById(Resource):
    @jwt_required()
    def get(self, id):
        '''Obtener menu por id'''
        controller = MenuController()
        return controller.getById(id)

    @jwt_required()
    @role_required(rol_id=1)
    @menu_ns.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Actualizar menu'''
        controller =MenuController()
        return controller.update(id, request.json)

    @jwt_required()
    @role_required(rol_id=1)
    def delete(self, id):
        '''Inhabilitar menu por ID'''
        controller = MenuController()
        return controller.delete(id)



