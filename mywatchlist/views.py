from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from mywatchlist.models import MyWatchList

# Create your views here.
def show_html(request):
    data = MyWatchList.objects.all()
    context = {
        'list_mywatchlist': data,
        'nama': 'Muhammad Reyvan Natechnoury',
        "npm": "2106654353",
    }
    return render(request, 'mywatchlist.html', context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")