from django.urls import path
from django.conf.urls import include
from webapp import views

urlpatterns = [
    path('', views.index, name='index'),
]
