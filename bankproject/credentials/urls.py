from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('apply',views.apply,name='apply'),
    path('form',views.form,name='form'),
    path('info',views.info,name="info")
]