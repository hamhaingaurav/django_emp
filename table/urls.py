from django.urls import path
from table.views import *

urlpatterns = [
    path('', home, name='home'),
    path('table/', table, name='table'),
    path('datatable/', datatable, name='datatable'),
    path('django-table/', DjangoTableView.as_view(), name='django_table'),
    path('download_data/', download_data, name='download_data')
]