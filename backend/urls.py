from django.urls import path
from .views import *

app_name = 'barang'
urlpatterns = [
    path('coba/', cobacoba, name='coba'),
	# path('detail_barang/<str:id>', detail_barang, name='detail_barang'),
]
