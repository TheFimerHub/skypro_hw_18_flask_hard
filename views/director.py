# загружаем все нужные библиотеки
from flask import request
from flask_restx import Resource, Namespace
from implemented import director_service
from dao.model.director import DirectorSchema

# создаем Namespace для вьюшек
director_ns = Namespace('directors')


# создаем вьюшку и класс с функциями
@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        objs = director_service.get_all()
        return DirectorSchema(many=True).dump(objs), 200

    def post(self):
        obj = director_service.create()
        return DirectorSchema().dump(obj), 201, {'location': f'/director/{obj.id}'}


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        obj = director_service.get_one(did)
        return DirectorSchema().dump(obj), 200

    def update(self, did):
        obj = director_service.update(did, request.json)
        return DirectorSchema().dump(obj), 200

    def delete(self, did):
        director_service.delete(did)
        return "Deleted", 204
