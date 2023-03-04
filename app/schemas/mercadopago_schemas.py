from flask_restx import fields

class MercadopagoRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def createUserTest(self):
        return self.namespace.model("Mecardopago User Test Create", {
            "description": fields.String(required=True)
        })
    