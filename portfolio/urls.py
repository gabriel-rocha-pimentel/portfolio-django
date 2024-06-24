from django.urls import path
from .views import home
from .views import categoria
from .views import portfolio
from .views import search

urlpatterns = [
    path('', home, name='home'),
    path('portfolio/', portfolio, name='portfolio'),
    path('categoria/<int:categoria_id>', categoria, name='categoria'),
    path('search/', search, name='search'),
]
