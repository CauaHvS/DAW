from django.urls import path
from .views import index, sobre, contato


urlpatterns = [
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='contato')
]
