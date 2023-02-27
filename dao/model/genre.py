# загружаем нужные библиотеки
from marshmallow import Schema, fields
from setup_db import db

# создаем модель
class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

# создаем схему
class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
