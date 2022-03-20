from django.urls import path
from . import views
 
urlpatterns=[
    path('',views.home,name= 'mainhome'),
    path('createquiz', views.createquiz, name = 'createquiz'),
    path('savequiz',views.savequiz, name = 'savequiz'),
    path('dashboard',views.dashboard,name = 'dashboard'),
    path('takequiz/<quiz_id>',views.takequiz,name = 'takequiz'),
    path('quizresult/<quiz_id>',views.takequiz,name = 'quizresult')
]