from django.shortcuts import render
from django.http import HttpResponse

def ex(request):
    return HttpResponse('<h2>Страница с картой</h2>')