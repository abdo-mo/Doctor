
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('login/', auth_views.LoginView.as_view(template_name = "login.html"), name = 'login'),
    path('settings/change_password/', auth_views.PasswordChangeView.as_view(template_name = "change_password.html"), name = 'password_change'),
    path('settings/change_password/done/', auth_views.PasswordChangeDoneView.as_view(template_name = "change_password_done.html"), name = 'password_change_done'),
    path('password-reset/',
            auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
            name = "password_reset"),
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name = "password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name = "password_reset_confirm"),
    path('password-reset_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name = "password_reset_complete"),
    # path('signup/ajax/validate_username/', views.validate_username, name = 'validate_username'),
    # path('acount/', views.profile, name = "my_acount"),
]