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

"""
table select_question
updated_at int(timestamp)
created_at int(timestamp)
id int(pk)
title char
answer_a char
answer_b char
answer_c char
answer_d char
correct_answer enum(a/b/c/d)
topic json(逻辑关联知识点)
hint char(提示) null
explain text(解释) null
hard int(难度系数几颗星)

"""




