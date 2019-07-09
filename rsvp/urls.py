from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('respond', views.respond, name='respond'),
    path('thanks', views.thanks, name='thanks'),
    path('contact', views.contact, name="contact-us"),
    path('message-sent', views.message_sent, name="message-sent"),
]
