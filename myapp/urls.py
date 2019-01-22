
from django.urls import path
from . import views

urlpatterns = [
    path('', views.greet, name="greet"),
    path('add_name', views.add_name, name="add_name"),
]