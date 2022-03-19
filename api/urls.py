from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_view

urlpatterns = [
    path('',views.guide , name = 'api_guide'),
    path('dashboard',views.dashboard , name = 'api_dashboard'),
    path('get_quiz/<str:pk>',views.get_quiz, name = 'api_get_quiz'),
    path('api_token_auth', auth_view.obtain_auth_token, name = 'api_get_token'),
    path('login',views.view_login,name ='api_login'),
    path('register',views.view_register, name = 'api_register'),
]