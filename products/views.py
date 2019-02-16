# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Product


def all_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})
