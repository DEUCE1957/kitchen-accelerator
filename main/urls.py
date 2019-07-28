from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('help', views.help, name='help'),
    path('error', views.error, name='error'),
    # MODERATOR VIEWS
    path('moderator',views.moderator,name='moderator'),
    path('edit_user', views.edit_user, name='edit_user'),
    path('invite', views.invite, name='invite'),
    # User Views
    path('user',views.user, name='user'),
    path('kitchen_status',views.kitchen_status, name='kitchen_status'),
    path('booking',views.booking, name='booking'),
    # Kitchen Views
    path('kitchens/', views.kitchen_overview, name="kitchens"),
    path('kitchen/<slug:kitchen_name_slug>', views.kitchen, name="kitchen"),
]