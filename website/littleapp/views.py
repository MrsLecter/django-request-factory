from django.shortcuts import redirect
from django.http import HttpResponse
import website.dataAccess


def index(request):
    return HttpResponse('ok')

def getInfo(request):
    data = website.dataAccess.getAllObject()
    return HttpResponse(data)

def postInfo(request, obj):
    if request.method == 'POST':
        website.dataAccess.postToDatabase(obj)
        return HttpResponse('add')

def toRedirect(request):
    return redirect('/get')

