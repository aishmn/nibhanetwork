from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
urlpatterns = [ 
    path("message-send/", views.send_message, name="send_message")
]