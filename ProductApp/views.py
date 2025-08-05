from django.shortcuts import render, redirect

from django.http import request

from ProductApp.models import Product


class products_id(request):
    products = Product.objects.all()


# Create your views here.
