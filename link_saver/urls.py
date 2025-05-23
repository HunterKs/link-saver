from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from bookmarks import views

urlpatterns = [
    path('', lambda request: redirect('login', permanent=False)),
    path('admin/', admin.site.urls),
    path('bookmarks/', include('bookmarks.urls')),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
]
