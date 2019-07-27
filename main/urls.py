from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('kitchen', views.kitchen, name="kitchen"),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout',views.user_logout, name='logout'),
    path('restricted',views.restricted, name='restricted')
]