from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_bookmark, name='add_bookmark'),
    path('register/', views.register, name='register'), 
    path('', views.list_bookmarks, name='list_bookmarks'),
    path('logout/', views.custom_logout, name='logout'),
    path('resummarize/<int:bookmark_id>/', views.resummarize_bookmark, name='resummarize_bookmark'),
]
