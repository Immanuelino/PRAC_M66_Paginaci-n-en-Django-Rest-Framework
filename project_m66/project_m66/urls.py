# project_m66/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import home_view  # Correctly import home_view from views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('', home_view, name='home'),  # Add this line for the homepage
]
