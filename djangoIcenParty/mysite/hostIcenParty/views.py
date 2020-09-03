from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Product, StatusBuy, BuyProduct
from .models import Genero
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def doBuyActive(request):
    if request.method == 'GET':
        address = request.GET['address']
        phone_contact = request.GET['phone_contact']
        allBuys = BuyProduct.objects.filter(address=address,
                                            phone_contact=phone_contact)
        dataBuys = serializers.serialize("json", list(allBuys),
                                         fields=('title',
                                                 'size',
                                                 'file_img_home',
                                                 'units',
                                                 'value',
                                                 'status_buy'),
                                         use_natural_foreign_keys=True,
                                         use_natural_primary_keys=True)
        r = str(dataBuys).replace("'", '')
        dataStoreArrayJSON = json.loads(r)
        data = {
            'success': True,
            'message': 'Consulta exitosa',
            'data': dataStoreArrayJSON
        }

        dump = json.dumps(data)
        return HttpResponse(dump.replace("\'", '"'), content_type='application/json')

    data = {
        'success': False,
        'message': 'Error al obtener información, not GET'
    }

    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def doProducts(request):
    if request.method == 'GET':
        if 'typeStore' in request.GET:
            typeStore = request.GET['typeStore']
            objectTypeStore = Genero.objects.get(name=typeStore)
            allStores = Product.objects.filter(type_store=objectTypeStore, is_active=True)
            dataStore = serializers.serialize("json", list(allStores),
                                              fields=('title',
                                                      'subTitle',
                                                      'description',
                                                      'file_img_home',
                                                      'file_img_2',
                                                      'file_img_3',
                                                      'material',
                                                      'brand',
                                                      'color',
                                                      'sizes_list',
                                                      'value'))
            r = str(dataStore).replace("'", '')
            dataStoreArrayJSON = json.loads(r)
            data = {
                'success': True,
                'message': 'Consulta exitosa',
                'stores': dataStoreArrayJSON
            }
            dump = json.dumps(data)
        else:
            data = {
                'success': False,
                'message': 'Error al obtener información'
            }
            dump = json.dumps(data)

        return HttpResponse(dump.replace("\'", '"'), content_type='application/json')

    data = {
        'success': False,
        'message': 'Error al obtener información, not GET'
    }
    dump = json.dumps(data)

    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def doAddBuy(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        objectStatusBuy = StatusBuy.objects.get(pk=body['pk_statusBuy'])
        objectProduct = Product.objects.get(pk=body['pk_product'])

        p = BuyProduct(phone_contact=body['phone'],
                       name_contact=body['name'],
                       city=body['city'],
                       neighborhood=body['neighborhood'],
                       address=body['address'],
                       type_house=body['typeHouse'],
                       units=body['units'],
                       value=body['value'],
                       size=body['size'],
                       file_img_home=body['file_img_home'],
                       status_buy=objectStatusBuy,
                       product_name=objectProduct)
        p.save()

        dataJson = {
            'success': True,
            'message': 'Se genero registro exitosamente'
        }

        dump = json.dumps(dataJson)
        return HttpResponse(dump.replace("\'", '"'), content_type='application/json')

    data = {
        'success': False,
        'message': 'Error al obtener información, not GET'
    }
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')
