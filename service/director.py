# создаем service класс для поддержки dao
class DirectorService:

    def __init__(self, dao):
        self.dao = dao

    def get_one(self, did):
        return self.dao.get_one(did)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, did):
        return self.dao.update(did)

    def delete(self, did):
        return self.dao.delete(did)
