# загружаем нужные библиотеки
from dao.model.director import Director

# создаем dao класс
class DirectorDAO:

    def __init__(self, session):
        '''
        загружаем session
        :param session:
        '''
        self.session = session

    def get_one(self, did):
        '''
        Выгрузка по одному объекту
        :param did: айди объекта
        :return: добавление по индексу
        '''
        return self.session.query(Director).get(did)

    def get_all(self):
        '''
        Добавляем всё из модели класса
        :return: всё из модели класса
        '''
        return self.session.query(Director).all()

    def create(self, data):
        '''
        Создаем и распаковываем данные
        :param data: поступившие данные
        :return: распакованный объект
        '''
        obj = Director(**data)

        self.session.add(obj)
        self.session.commit()

        return obj

    def update(self, did, data):
        '''
        Обновляем данные по индексу
        :param did: айди объекта
        :param data: поступившие данные
        '''
        obj = self.get_one(did)

        obj.name = data.get('name')

        self.session.add(obj)
        self.session.commit

    def delete(self, did):
        '''
        Удаляем данные по айди
        :param did: айди объекта
        '''
        obj = self.get_one(did)
        self.session.delete(obj)
        self.session.commit()
