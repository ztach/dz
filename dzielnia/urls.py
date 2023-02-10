from django.urls import path

from . import views

app_name ='dzielnia'

urlpatterns = [
    path('', views.index, name='index'),
]