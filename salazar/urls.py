
from django.contrib import admin
from django.urls import path
from  . import views
from mainapp import views



urlpatterns = [
    path('hola/', views.index),
    path('admin/', admin.site.urls),
    path('', views.index),
]
