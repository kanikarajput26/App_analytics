from __future__ import unicode_literals
from mongoengine import *

class Rank(Document):
    app_name = StringField()
    country = StringField()
    category_rank = StringField()
    topchart_rank = StringField()
    cid = StringField()


