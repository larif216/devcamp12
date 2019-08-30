from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def cobacoba(request):
    body = json.loads(request.body.decode('utf-8'))

    products = body['product']
    regional = body['regional']

    predictions = []
    for product in products:
        # process
        break

    responseData = {
        'city': products[1],
        'data': {
            'merk': body['product']
        } 
    }

    return JsonResponse(responseData)