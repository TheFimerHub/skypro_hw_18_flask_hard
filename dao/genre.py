# загружаем нужные библиотеки
from dao.model.genre import Genre

# создаем dao класс
class GenreDAO:

    def __init__(self, session):
        '''
        загружаем session
        :param session:
        '''
        self.session = session

    def get_one(self, gid):
        '''
        Выгрузка по одному объекту
        :param gid: айди объекта
        :return: добавление по индексу
        '''
        return self.session.query(Genre).get(gid)

    def get_all(self):
        '''
        Добавляем всё из модели класса
        :return: всё из модели класса
        '''
        return self.session.query(Genre).all()

    def create(self, data):
        '''
        Создаем и распаковываем данные
        :param data: поступившие данные
        :return: распакованный объект
        '''
        obj = Genre(**data)

        self.session.add(obj)
        self.session.commit()

        return obj

    def update(self, gid, data):
        '''
        Обновляем данные по индексу
        :param gid: айди объекта
        :param data: поступившие данные
        '''
        obj = self.get_one(gid)

        obj.name = data.get('name')

        self.session.add(obj)
        self.session.commit

    def delete(self, gid):
        '''
        Удаляем данные по айди
        :param gid: айди объекта
        '''
        obj = self.get_one(gid)
        self.session.delete(obj)
        self.session.commit()
