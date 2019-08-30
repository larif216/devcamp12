import requests
import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Merk, Product, Voucher
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def cobacoba(request):
    # body = json.loads(request.body.decode('utf-8'))

    # products = body['product']
    # regional = body['regional']

    responseData = {'a': 0}

    # predictions = []
    # for product in products:
    #     # process
    #     break

    # responseData = {
    #     'city': products[1],
    #     'data': {
    #         'merk': body['product']
    #     } 
    # }

    return JsonResponse(responseData)

def getProductList(request):
    return JsonResponse({
        'product': [
            {
                'key': key,
                'name': product['name']
            }
            for key, product in products.items()
        ]
    })

categories = {
    1: {'name': 'smartphone'},
    2: {'name': 'laptop'}
}

merks = {
    1: {'name': 'Samsung M20'},
    2: {'name': 'Realme 3 Pro'},
    3: {'name': 'Macbook Pro 2017'}
}

products = {
    1: {
        'merk_id': 1,
        'category_id': 1,
        'name': 'Samsung M20'
    },
    2: {
        'merk_id': 2,
        'category_id': 1,
        'name': 'Realme 3 Pro'
    },
    3: {
        'merk_id': 3,
        'category_id': 2,
        'name': 'Macbook Pro 2017'
    }
}