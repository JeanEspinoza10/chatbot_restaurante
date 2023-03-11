from app import db
from app.models.menu_model import Menu
from app.schemas.menu_schemas import MenuResponseSchema
from flask_jwt_extended import current_user
import datetime


class MenuController:
    def __init__(self):
        self.model = Menu
        self.schema = MenuResponseSchema
        self.current_user = current_user

    def all(self, query):
        try:
            page = query['page']
            per_page = query['per_page']
            current_date = datetime.date.today().strftime("%Y-%m-%d")
            print(current_date)
            records = self.model.where(fecha=current_date, disonibilidad=True).order_by('id').paginate(
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
                'message': 'El producto se creo con exito'
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
                'message': 'No se encontro el producto'
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
                    'message': f'El producto {id}, ha sido actualizado'
                }, 200
            return {
                'message': 'No se encontro el producto mencionado'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def delete(self, id):
        try:
            record = self.model.where(id=id).first()
            if record and record.status:
                record.update(status=False)
                db.session.add(record)
                db.session.commit()
                return {
                    'message': f'El producto {id}, ha sido deshabilitado'
                }, 200
            return {
                'message': 'No se encontro el producto mencionado'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500


        