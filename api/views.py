from django.http import HttpResponse
from . import models
import simplejson
from . import utils
from pymongo import MongoClient

client = MongoClient("85.25.137.38")
db = client.appdb
collect1 = db.VarStats

def getRank(request):
    id = request.GET['id']
    g1 = utils.Processor(collect1, id)
    new_list=[]
    for item in g1:
        app_name = item['app_name']
        category_rank = item['category_rank']
        topchart_rank = item['topchart_rank']
        country = item['_id']['country']
        cid = item['_id']['id']
        new_list.append({"app_name":app_name,"category_rank":category_rank,"topchart_rank":topchart_rank,"cid":cid,"country":country})
    return HttpResponse(simplejson.dumps(new_list),content_type='application/json')


