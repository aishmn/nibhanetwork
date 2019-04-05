from django.urls import path,include
from . import views

##patth
urlpatterns = [
    path('', views.index, name='home'),
    # path('terms/', views.terms, name='terms')
]
