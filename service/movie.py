# создаем service класс для поддержки dao
class MovieService:

    def __init__(self, dao):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, filters=None):
        return self.dao.get_all(filters)

    def create(self, data):
        return self.dao.create(data)

    def update(self, mid):
        return self.dao.update(mid)

    def delete(self, mid):
        return self.dao.delete(mid)
