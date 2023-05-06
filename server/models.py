import time

from peewee import *


db = SqliteDatabase("fish.db")


class BaseModel(Model):
    created_at = IntegerField(default=time.time)
    updated_at = IntegerField(default=time.time)

    class Meta:
        database = db


class People(BaseModel):
    name = CharField()
    age = IntegerField()





