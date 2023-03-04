from app import api
from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required
from app.helpers.decorators import role_required
from app.schemas.categoria_schemas import CategoriaRequestSchema
from app.controllers.categoria_controller import CategoriaController

cateogira_ns = api.namespace(
    name="Categorias de productos",
    description ="Ruta para añadir las categorias",
    path = "/categorias"
)

request_schema = CategoriaRequestSchema(cateogira_ns)

@cateogira_ns.route("")
class Categoria(Resource):
    @cateogira_ns.expect(request_schema.all())
    def get(self):
        '''Listar todas la categorias'''
        query = request_schema.all().parse_args()
        controller = CategoriaController()
        return controller.all(query)
    
    # Creacion de categorias
    @cateogira_ns.doc(security="Bearer")
    @jwt_required()
    @role_required(rol_id=1)
    @cateogira_ns.expect(request_schema.create(), validate=True)
    def post (self):
        '''Creacion de Categorias'''
        controller = CategoriaController()
        return controller.create(request.json)
    

@cateogira_ns.route("/<int:id>")
@cateogira_ns.doc(security ="Bearer")
class CategoriaById(Resource):
    @jwt_required()
    def get(self, id):
        '''Obtener categoria por id'''
        controller = CategoriaController()
        return controller.getById(id)
    
    @jwt_required()
    @role_required(rol_id=1)
    @cateogira_ns.expect(request_schema.update(), validate= True)
    def put(self, id):
        '''Actualizar categoria'''
        controller = CategoriaController()
        return controller.update(id, request.json)

    @jwt_required()
    @role_required(rol_id=1)
    def delete(self, id):
        '''Inhabilitar menu por ID'''
        controller = CategoriaController()
        return controller.delete(id)