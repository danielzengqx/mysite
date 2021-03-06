from django.db import models
from mongoengine import *
from mysite.settings import DBNAME

connect(DBNAME)

class Post(Document):
    title = StringField(max_length=120, required=True)
    test_type = StringField(max_length=100, required=True)
    content = StringField(max_length=500, required=True)
    last_update = DateTimeField(required=True)
