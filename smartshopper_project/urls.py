from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),   # root → frontend
    path('api/', include('products.urls'))  # keep API prefix too
]
