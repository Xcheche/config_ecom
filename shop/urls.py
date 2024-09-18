from django.urls import path

# from .views import ProductView
from . import views

urlpatterns = [
    # path("", ProductView.as_view(), name="home"),
    path("", views.index, name="home"),
]
