from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name='auth_links'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page="accounts/logout.html"), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
]
