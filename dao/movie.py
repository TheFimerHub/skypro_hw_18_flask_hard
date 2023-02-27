# загружаем нужные библиотеки
from dao.model.movie import Movie

# создаем dao класс
class MovieDAO:

    def __init__(self, session):
        '''
        загружаем session
        :param session:
        '''
        self.session = session

    def get_one(self, mid):
        '''
        Выгрузка по одному объекту
        :param mid: айди объекта
        :return: добавление по индексу
        '''
        return self.session.query(Movie).get(mid)

    def get_all(self, filters=None):
        '''
        Добавляем всё из модели класса и
        может быть фильтрацию
        :return: все данные из модели класса
        (может быть фильтрованные)
        '''
        query = self.session.query(Movie)

        if filters and (director_id := filters.get('director_id')):
            query = query.filter(Movie.director_id == director_id)

        if filters and (genre_id := filters.get('genre_id')):
            query = query.filter(Movie.genre_id == genre_id)

        if filters and (year := filters.get('year')):
            query = query.filter(Movie.year == year)

        return query.all()

    def create(self, data):
        '''
        Создаем и распаковываем данные
        :param data: поступившие данные
        :return: распакованный объект
        '''
        obj = Movie(**data)

        self.session.add(obj)
        self.session.commit()

        return obj

    def update(self, mid, data):
        '''
        Обновляем данные по индексу
        :param mid: айди объекта
        :param data: поступившие данные
        '''
        obj = self.get_one(mid)

        obj.name = data.get('title')
        obj.name = data.get('description')
        obj.name = data.get('trailer')
        obj.name = data.get('year')
        obj.name = data.get('rating')

        self.session.add(obj)
        self.session.commit

    def delete(self, mid):
        '''
        Удаляем данные по айди
        :param mid: айди объекта
        '''
        obj = self.get_one(mid)
        self.session.delete(obj)
        self.session.commit()
