from django.shortcuts import render
from django.http import JsonResponse
from .models import Wigs
from .serializers import WigSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def wig(request):
    if request.method == 'GET':
        wigs = Wigs.objects.all()
        serializer = WigSerializer(wigs, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = WigSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def wig_detail(request, pk):
    try:
        wig = Wigs.objects.get(id=pk)
    except Wigs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WigSerializer(wig)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = WigSerializer(wig, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        wig.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)