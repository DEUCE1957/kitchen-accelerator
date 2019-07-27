from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('kitchen', views.kitchen, name="kitchen"),
    path('restricted',views.restricted, name='restricted')
]