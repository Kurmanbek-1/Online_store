from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse
from datetime import datetime
from HW.models import Product, Hashtag

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
            'products': [
                {
                    'image': product.image,
                    'title': product.title,
                    'description': product.description,
                    'rate': product.rate,
                    'hashtag': product.hashtags,
                } for product in products
            ]
        }
        return render(request, 'products/products.html', context=context)


def hashtags_view(request):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()

        context = {
            'hashtags': hashtags
        }

        return render(request, 'products/hashtags.html', context=context)