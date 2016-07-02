from django.core.management.base import BaseCommand, CommandError
import api.utils as utils
import api.views as views
from pymongo import MongoClient

client = MongoClient("85.25.137.38")
db = client.appdb
collect1 = db.VarStats


class Command(BaseCommand):
    help = "it saves app data."

    def handle(self, *args, **options):
        cid = views.id
        g1 = utils.Processor(collect1,cid)
        for item in g1:
            utils.Saver(item)
        return