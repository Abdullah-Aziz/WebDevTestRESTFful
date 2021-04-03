from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductForm, RetrieveForm, UpdateForm

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

# Create your views here.


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Create': '/product_create/',
        'Retrieve': '/product_detail/',
        'Update': '/product_update/',
        'List_Sold': '/product_sold/',
        'List_Remaining': '/product_remaining/'
    }
    return Response(api_urls)


@api_view(['GET'])
def product_list(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_retrieve(request, pk):
    products = Products.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def product_create(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def product_update(request, pk):
    product = Products.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def product_sold(request):
    products = Products.objects.all()
    sold = []

    for product in products:
        if product.QTY == 0:
            # What to show?
            sold.append(product)
    serializer = ProductSerializer(sold, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_remaining(request):
    products = Products.objects.all()
    remaining = []

    for product in products:
        if product.QTY > 0:
            # What to show?
            remaining.append(product)
    serializer = ProductSerializer(remaining, many=True)
    return Response(serializer.data)
