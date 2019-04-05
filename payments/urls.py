from django.urls import path,include
from . import views
##patth
urlpatterns = [
   	path('closing/', views.do_closing_view, name='do-closing'),
   	path('management/', views.payments_management_view, name='payment-management'),
	path('paid/', views.ammount_paid, name='paid')
	
 ]
