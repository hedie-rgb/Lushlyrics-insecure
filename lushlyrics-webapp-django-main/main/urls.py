from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.default, name='default'),
    path("restricted/", views.restricted, name='restricted'),
    path("login/", views.login, name='login'),
    path("signup/", views.signup, name='signup'),
    path("playlist/", views.playlist, name='your_playlists'),
    path("search/", views.search, name='search_page') 
]