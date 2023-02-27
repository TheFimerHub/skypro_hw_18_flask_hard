# загружаем все нужные библиотеки
from flask import request
from flask_restx import Resource, Namespace
from implemented import movie_service
from dao.model.movie import MovieSchema

# создаем Namespace для вьюшек
movie_ns = Namespace('movies')


# создаем вьюшку и класс с функциями
@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        filters = dict()
        if director_id := request.args.get('director_id'):
            filters['director_id'] = director_id

        if genre_id := request.args.get('genre_id'):
            filters['genre_id'] = genre_id

        if year := request.args.get('year'):
            filters['year'] = year

        objs = movie_service.get_all(filters=filters)
        return MovieSchema(many=True).dump(objs), 200

    def post(self):
        obj = movie_service.create()
        return MovieSchema().dump(obj), 201, {'location': f'/genre/{obj.id}'}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        obj = movie_service.get_one(mid)
        return MovieSchema().dump(obj), 200

    def update(self, mid):
        obj = movie_service.update(mid, request.json)
        return MovieSchema().dump(obj), 200

    def delete(self, mid):
        movie_service.delete(mid)
        return "Deleted", 204
