from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path("index", views.index),
    path("demo",views.demo),
    path("search",views.search),
    path("all",views.all),
    path("sessionset", views.sessionset),
    path("sessionget", views.sessionget),
    path("sessionview", views.sessionview),
]