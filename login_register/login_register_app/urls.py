from django.urls import path,include
from . import views
app_name = 'register_login'
urlpatterns = [
    path('',views.index),
    path('register',views.register,name='register'),
    path('success/<int:id>',views.success,name='success'),
    path('login',views.login,name='login'),
    path('logout/<int:id>',views.logout,name='logout'),
]
