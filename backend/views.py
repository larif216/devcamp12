import requests
import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Merk, Product, Voucher, Regional
from django.views.decorators.csrf import csrf_exempt
import datetime

@csrf_exempt
def getPrediction(request, id, regional):

    responseData = {'a': id, 'b': str(Category.objects.get(id=1).name)}

    return JsonResponse(responseData)

def getProductList(request):
    return JsonResponse({
        'product': [
            {
                'key': product.id,
                'value': product.name
            }
            for product in Product.objects.all()
        ]
    })

def getRegionalList(request):
    return JsonResponse({
        'regional': [
            {
                'key': regional.id,
                'name': regional.name
            }
            for regional in Regional.objects.all()
        ]
    })