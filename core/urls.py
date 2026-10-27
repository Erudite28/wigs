from django.urls import path
from .views import wig

urlpatterns = [
    path('wigs/', wig, name='wigs')
]