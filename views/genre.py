# загружаем все нужные библиотеки
from flask import request
from flask_restx import Resource, Namespace
from implemented import genre_service
from dao.model.genre import GenreSchema

# создаем Namespace для вьюшек
genre_ns = Namespace('genres')


# создаем вьюшку и класс с функциями
@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        objs = genre_service.get_all()
        return GenreSchema(many=True).dump(objs), 200

    def post(self):
        obj = genre_service.create()
        return GenreSchema().dump(obj), 201, {'location': f'/genre/{obj.id}'}


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        obj = genre_service.get_one(gid)
        return GenreSchema().dump(obj), 200

    def update(self, gid):
        obj = genre_service.update(gid, request.json)
        return GenreSchema().dump(obj), 200

    def delete(self, gid):
        genre_service.delete(gid)
        return "Deleted", 204
