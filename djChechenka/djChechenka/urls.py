from django.contrib import admin
from django.urls import path, include

#Здесь оставляем ссылки
# path('ПУТЬ', include('НАЗВАНИЕ_ПРИЛОЖЕНИЯ.urls'))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('reg/', include('register.urls')),
    path('map/', include('couriermap.urls')),
]
