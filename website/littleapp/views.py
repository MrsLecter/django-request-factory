from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
import website.dataAccess
from littleapp import models

def index(request):
    return HttpResponse('ok')

def getInfo(request):
    data = website.dataAccess.getAllObject()
    return HttpResponse(data)

def postInfo(request, obj):
    if request.method == 'POST':
        website.dataAccess.postToDatabase(obj)
        return JsonResponse({"method": "POST", "message": "add"})

def toRedirect(request):
    return redirect('/get')

def toGetBasket(request):
    if request.method == 'GET':
        return JsonResponse({"method": "GET", "route": "/basket/<int:object_id>/"})
    else:
        item = models.Basket(name=request.POST['name'], description=request.POST['description'])
        item.save()
        count = models.Basket.objects.count()
        return JsonResponse({'status': 'created', 'goods_amount': count, 'add_item': item.id})

def toGetItemById(request, item_id):
    current_item = models.Basket.objects.get(id = item_id)
    return JsonResponse({'status': 'ok', 'data': current_item})

