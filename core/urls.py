from django.urls import path
from .views import index,contato,produtos

urlpatterns = [
    path('', index),
    path('contato', contato),
    path('produtos', produtos),

]
