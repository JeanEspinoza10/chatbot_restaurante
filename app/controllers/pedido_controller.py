from app import db
from app.models.pedido_model import PedidoModel
from app.schemas.pedido_schemas import PedidoResponseSchema
from flask_jwt_extended import current_user
import datetime


class PedidoController:
    def __init__(self):
        self.model = PedidoModel
        self.schema = PedidoResponseSchema
        self.current_user = current_user
    
    def all(self, query):
        try:
            page = query['page']
            per_page = query['per_page']
            current_date = datetime.date.today().strftime("%Y-%m-%d")
            records = self.model.where(estado = "En proceso",fecha=current_date ).order_by('id').paginate(
                page=page, per_page=per_page
            )

            response = self.schema(many=True)

            return {
                'results': response.dump(records.items),
                'pagination': {
                    'totalRecords': records.total,
                    'totalPages': records.pages,
                    'perPage': records.per_page,
                    'currentPage': records.page
                }
            }, 200
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500
    

    def create(self, data):
        try:
            new_record = self.model.create(**data)
            db.session.commit()

            return {
                'message': 'El pedido se creo con exito'
            }, 201
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def getById(self, id):
        try:
            record = self.model.where(id=id).first()
            if record:
                response = self.schema(many=False)
                return response.dump(record), 200
            return {
                'message': 'No se encontro el pedido mencionado'
            }, 404
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500
    
    def update(self, id, data):
        try:
            record = self.model.where(id=id).first()
            if record:
                record.update(**data)
                db.session.add(record)
                db.session.commit()
                return {
                    'message': f'El pedido {id}, ha sido actualizado'
                }, 200
            return {
                'message': 'No se encontro el pedido mencionado'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500
    
    def profileMe(self):
        try:
            user_id = self.current_user.id
            print(user_id)
            record = self.model.where(user_id=user_id).first()
            if record:
                response = self.schema(many=False)
                return response.dump(record), 200
            return {
                'message': 'No se encontro los pedidos asosciados al usuario'
            }, 404
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500
    
