from django.shortcuts import render

def ex(request):
    return render(request, 'main/index.html')