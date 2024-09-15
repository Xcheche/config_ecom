from django.shortcuts import render
from .models import Product
from django.views.generic import ListView  # new

# Create your views here.


class ProductView(ListView):
    model = Product
    template_name = "shop/index.html"
    context_object_name = "products"
