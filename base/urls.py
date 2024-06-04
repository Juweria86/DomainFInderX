from django.urls import path
from .views import domain_search_view, home_view

urlpatterns = [
path('', home_view, name='home'),
path('domain-search/', domain_search_view, name='domain_search'),
]