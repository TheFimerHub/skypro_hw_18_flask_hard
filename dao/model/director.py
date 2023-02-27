# загружаем нужные библиотеки
from marshmallow import Schema, fields
from setup_db import db

# создаем модель
class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

# создаем схему
class DirectorSchema(Schema):
    __tablename__ = 'director'
    id = fields.Int()
    name = fields.Str()
