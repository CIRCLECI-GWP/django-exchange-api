from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:currency>', views.rates, name='rates')
]