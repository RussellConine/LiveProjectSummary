from django.urls import path
from . import views

urlpatterns = [
    # sets the url path to home page skis_home.html
    path('', views.skis_home, name='skis_home'),
    # sets path to page to create new ski item
    path('create/', views.create_ski, name='create_ski'),
    # sets the url path to read all items in database
    path('viewall/', views.read_skis, name='read_all_skis'),
    # sets the url path to view a specific ski, based on primary key of that ski
    path('<int:pk>/details/', views.ski_details, name='details'),
    # sets the url path to view weather from nws api
    path('weather_check/', views.check_weather, name='weather_check'),
    # sets the url path to edit a specific ski, based on primary key of that ski
    path('<int:pk>/edit/', views.edit_ski, name='ski_edit'),
    # sets the url path to confirm and delete a specific ski
    path('<int:pk>/delete/', views.delete_ski, name='delete_ski'),
]
