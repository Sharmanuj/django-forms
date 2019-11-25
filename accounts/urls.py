from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth.views import (
    PasswordResetDoneView,
    PasswordResetConfirmView,
)


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='registration/logged_out.html'), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    path('profile/', views.View_profile.as_view(), name='view_profile'),
    path('profile/<int:pk>/', views.View_profile.as_view(), name='view_profile_with_pk'),
    path('profile/edit/', views.Edit_profile.as_view(), name='edit_profile'),
    path('change-password/', views.Change_password.as_view(), name='change_password'),
    path('reset-password/done/', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    

]
