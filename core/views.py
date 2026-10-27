from django.shortcuts import render
from django.http import JsonResponse
from .models import Wigs
from .serializers import WigSerializer

# Create your views here.
def wig(request):
    wigs = Wigs.objects.all()
    serializer = WigSerializer(wigs, many=True)
    return JsonResponse(serializer.data, safe=False)