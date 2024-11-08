# products/views.py
from rest_framework.generics import ListAPIView
from .models import Product
from .serializers import ProductSerializer
from .pagination import CustomPageNumberPagination  # Use the chosen pagination class
from django.http import HttpResponse

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination  # Set your pagination class here

# project_m66/views.py

def home_view(request):
    return HttpResponse("<h1>Welcome to project_m66 API</h1>")