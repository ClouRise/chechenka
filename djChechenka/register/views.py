from django.shortcuts import render
from django.http import HttpResponse

def ex(request):
    return HttpResponse('<h2>Регистрация</h2>')