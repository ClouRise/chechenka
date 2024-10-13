from django.shortcuts import render

def ex(request):
    return render(request, 'registration/index.html')