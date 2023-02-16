from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse
from datetime import datetime
from HW.models import Product

def hello(request):
    if request.method == "GET":
        return HttpResponse('Hello! Its my project')


def now_date(request):
    if request.method == 'GET':
        return HttpResponse(datetime.now())

def goodbay(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')

def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'products/products.html', context=context)