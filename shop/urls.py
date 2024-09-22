from django.urls import path

# from .views import ProductView
from . import views

urlpatterns = [
    # path("", ProductView.as_view(), name="home"),
    path("", views.index, name="home"),
    path("product_detail/<int:id>", views.product_detail, name="product_detail"),
]
