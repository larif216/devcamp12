from django.urls import path
from .views import getProductList, getRegionalList, getPrediction

app_name = 'barang'
urlpatterns = [
    path('product/', getProductList, name='product'),
    path('regional/', getRegionalList, name='regional'),
    path('predict/<str:id>/', getPrediction, name='predict'),
]
