
from django.urls import path, include



urlpatterns = [
    path('entrar/', include('django.contrib.auth.login',
                            {'template_name': 'accounts/login.html'},
                            namespace='login')),
]

