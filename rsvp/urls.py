from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('respond', views.respond, name='respond'),
    path('thanks', views.thanks, name='thanks'),
]
