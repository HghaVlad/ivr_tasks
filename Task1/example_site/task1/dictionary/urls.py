from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path("", views.home_page),
   path("home", views.home_page),
   path("add_word", views.add_word),
   path("words_list", views.words_list)
]