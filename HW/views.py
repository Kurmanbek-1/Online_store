# from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse
from datetime import datetime

def hello(request):
    if request.method == "GET":
        return HttpResponse('Hello! Its my project')


def now_date(request):
    if request.method == 'GET':
        return HttpResponse(datetime.now())

def goodbay(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')




