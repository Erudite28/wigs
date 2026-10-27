from django.urls import path
from .views import wig, wig_detail

urlpatterns = [
    path('wigs/', wig, name='wigs'),
    path('wigs/<int:pk>/', wig_detail, name='wigs'),
]