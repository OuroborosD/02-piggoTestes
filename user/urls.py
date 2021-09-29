from django.urls import path
from . import views


urlpatterns =[
    path('', views.cadastrar, name='user_cadastro'),
    path('login/', views.login, name='user_login'),
    path('dashboard/',views.dashboard,name='user_dashboard'),
]