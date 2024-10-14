from django.urls import path
from . import views

urlpatterns = [
    path('', views.ex),
    path('map/', views.map),
]
