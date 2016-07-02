from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'appanalytics/',views.getRank,name="analytics"),
]