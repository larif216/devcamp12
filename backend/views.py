import requests, json, datetime, os
import pickle, pandas as pd, numpy as np
from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Merk, Product, PlannedVoucher, Regional, Purchase
from django.views.decorators.csrf import csrf_exempt

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

@csrf_exempt
def getPrediction(request, id):
    region_datas = []
    for regional in Regional.objects.all():
        product = Product.objects.get(id=id)
        resultMerk, resultCategory = predictLineChart(product, regional.id)

        temp = {
            'id': regional.id,
            'name': regional.name,
            'sum': sum(resultMerk),
            'time': {
                'merk': resultMerk,
                'category': resultCategory
            }
        }
        region_datas.append(temp)

    responseData = {
        'name': product.name,
        'region': region_datas
    }

    return JsonResponse(responseData)

def predictLineChart(product, regional):
    delta_days =  (datetime.date.today() - product.model_time).days

    filename = './backend/models/merk-' + str(product.id) + '-' + str(regional) + '.pkl'
    filename2 = './backend/models/category-' + str(product.id) + '-' + str(regional) + '.pkl'

    if (delta_days > 2) | (not os.path.isfile(filename)) | (not os.path.isfile(filename2)):
        model = createModelMerk(product, regional)
        pickle.dump(model, open(filename, 'wb'))

        model2 = createModelCategory(product, regional)
        pickle.dump(model2, open(filename2, 'wb'))

        product.model_time = datetime.date.today()
        product.save()
    else:
        model = pickle.load(open(filename, 'rb'))
        model2 = pickle.load(open(filename2, 'rb'))

    return (
        predictDemand(model, product, regional), 
        predictDemand(model2, product, regional)
    )

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
                'value': regional.name
            }
            for regional in Regional.objects.all()
        ]
    })

def createModelMerk(product, regional_id):
    train_data, train_label = arrangeData(
        Purchase.objects.filter(
            merk_id = product.merk_id.id,
            regional_id = regional_id
        )
    )
    return RandomForestRegressor(random_state=1)\
        .fit(train_data, train_label)

def createModelCategory(product, regional_id):
    train_data, train_label = arrangeData(
        Purchase.objects.filter(
            category_id = product.category_id.id,
            regional_id = regional_id
        )
    )
    return RandomForestRegressor(random_state=1)\
        .fit(train_data, train_label)

def arrangeData(purchases):
    train_data = [
        [
            int(e.time.month),
            int(e.time.day),
            int(e.time.weekday())
        ] for e in purchases
    ]
    train_label = [
        e.count
        for e in purchases
    ]
    return (train_data, train_label)

def predictDemand(model, product, regional):
    start_date = datetime.date.today()
    dates = [start_date + datetime.timedelta(days=x) for x in range(90)]
    
    test_data = [
        [
            int(e.month),
            int(e.day),
            int(e.weekday())
        ] for e in dates
    ]
    return [int(e) for e in model.predict(test_data)]