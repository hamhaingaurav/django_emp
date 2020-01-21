from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('download_data/',views.download_data,name='download_data')
]