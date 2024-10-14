from django.shortcuts import render

def ex(request):
    return render(request, 'couriermap/index.html')
def map(request):
    return render(request, 'couriermap/map.html')