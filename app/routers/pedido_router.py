from app import api
from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required
from app.helpers.decorators import role_required
from app.schemas.pedido_schemas import PedidoRequestSchema
from app.controllers.pedido_controller import PedidoController
from datetime import datetime

pedido_ns = api.namespace(
    name = "Pedido",
    description ="Ruta para los pedidos",
    path = "/pedidos"
)

request_schema = PedidoRequestSchema(pedido_ns)

@pedido_ns.route("")
class Pedido(Resource):
    @pedido_ns.expect(request_schema.all())
    def get(self):
        '''Lista de pedidos activos'''
        query = request_schema.all().parse_args()
        controller = PedidoController()
        return controller.all(query)
    
    # Creacion
    @pedido_ns.doc(security = "Bearer")
    @jwt_required()
    @role_required(rol_id=1)
    @pedido_ns.expect(request_schema.create())
    def post(self):
        '''Creacion del pedido'''
        controller = PedidoController()
        return controller.create(request.json)
    
@pedido_ns.route("/<int:id>")
class PedidoById(Resource):
    def get(self, id):
        '''Obtener pedido por un id'''
        controller = PedidoController()
        return controller.getById(id)
    
    #Actualizar por id
    @pedido_ns.doc(security = "Bearer")
    @jwt_required()
    @role_required(rol_id=1)
    @pedido_ns.expect(request_schema.update(), validate=True)
    def put(self, id):
        '''Actualizar por id'''
        controller=PedidoController()
        return controller.update(id, request.json)

@pedido_ns.route("/pedidos_asociados")
@pedido_ns.doc(security="Bearer")
class PedidoByProfile(Resource):
    @jwt_required()
    def get(self):
        '''Obtener los pedidos del usuario conectado'''
        controller = PedidoController()
        return controller.profileMe()
    