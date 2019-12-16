from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from simplemooc.accounts.views import register, dashboard, edit, edit_password
from django.contrib.auth import views as auth_views
from django.urls import path, include

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('painel/', dashboard, name='dashboard'),
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('sair/', LogoutView.as_view(next_page='home'), name='logout'),
    path('cadastro/', register, name='register'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html', email_template_name='accounts/password_reset_email.html', success_url='password_reset_done'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(success_url ='password_reset_complete'), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
    path('editar/', edit, name='edit'),
    path('editar-senha/', edit_password, name='edit_password'),
]