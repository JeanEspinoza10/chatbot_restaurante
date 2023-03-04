from app import api
from flask_restx import Resource
from app.schemas.mercadopago_schemas import MercadopagoRequestSchema
from app.utils.mercadopago import MercadoPago

mercado_ns = api.namespace(
    name= "Mercado pago",
    description ="Rutas para la integracion con mercado pago",
    path="/mercadopago"
)
request_schema = MercadopagoRequestSchema(mercado_ns)

@mercado_ns.route("/users/test")
class UserTest(Resource):
    @mercado_ns.expect(request_schema.createUserTest(), validate=True)
    def post(self):
        '''Crear usuario de prueba'''
        mercadopago = MercadoPago()
        return mercadopago.createUserTest(mercado_ns.payload)