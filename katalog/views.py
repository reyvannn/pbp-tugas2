from django.shortcuts import render

from katalog.models import CatalogItem

def show_katalog(request):
    return render(request, 'katalog.html', context)

data_catalog_item = CatalogItem.objects.all()
context = {
    'list_katalog': data_catalog_item,
    'nama': 'Muhammad Reyvan Natechnoury',
    "npm" : "2106654353",
}