from django.urls import path
from .views import domain_search_view

urlpatterns = [
path('', domain_search_view, name='domain_search'),
]