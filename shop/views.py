from django.shortcuts import render
from .models import Product

# from django.views.generic import ListView  # new
from django.core.paginator import Paginator


# Create your views here.


# class ProductView(ListView):
#     model = Product
#     template_name = "shop/index.html"
#     context_object_name = "products"


def index(request):
    products = Product.objects.all()
    # Search Logic
    q = request.GET.get("q")
    if q != "" and q is not None:
        products = (
            products.filter(title__icontains=q)
            | products.filter(price__icontains=q)
            | products.filter(description__icontains=q)
            | products.filter(category__icontains=q)
        )

    # Paginator
    pagiantor = Paginator(products, 3)
    page = request.GET.get("page")
    products = pagiantor.get_page(page)
    context = {"products": products, "q": q}
    return render(request, "shop/index.html", context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, "shop/product_detail.html", {"product": product})
