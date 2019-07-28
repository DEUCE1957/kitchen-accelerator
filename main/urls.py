from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('status_page',views.status, name='status_page'),
    path('user',views.user, name='user'),
    path('about/', views.about, name='about'),
    path('kitchens/',views.kitchen_overview, name="kitchens"),
    path('kitchen/<slug:kitchen_name_slug>', views.kitchen, name="kitchen"),
    path('restricted',views.restricted, name='restricted'),
]