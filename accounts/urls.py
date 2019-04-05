from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
urlpatterns = [
    path("activate/", views.activate_view , name="activate"),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path("user_profile/", views.profile_view, name="user-profile"),
    path("user-settings/", views.user_settings_veiw, name="user-settings"),
    path("payments/", views.payments_view, name="payments"),
    path('payments/withdraw/',views.withdraw_view, name = 'withdraw'),
    path('register/<slug:user>/', views.register, name = 'refer_user'),
]
