from django.urls import path
from .views import frontend_home, search_products, all_products

urlpatterns = [
    path('', frontend_home, name='frontend_home'),             # /api/
    path('search/', search_products, name='search_products'),  # /api/search/
    path('all/', all_products, name='all_products'),           # /api/all/
]
