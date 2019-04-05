from django.urls import path,include
from . import views

#path
urlpatterns = [
    path('create', views.create_epin_view, name='create_epin'),
    path('management', views.epin_management_view, name='epin_management')
    ]
