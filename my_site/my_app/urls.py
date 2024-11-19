from django.urls import path
from . import views

# domaion.com/my_app/simple_view
urlpatterns = [
    path('', views.simple_view) #/my_apps --> PROJECT urls.py
]
