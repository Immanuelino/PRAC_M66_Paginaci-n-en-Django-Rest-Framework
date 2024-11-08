from django.http import HttpResponse
from django.urls import reverse

def home_view(request):
    html_content = """
    <h1>Welcome to project_m66 API</h1>
    <p>Navigate to:</p>
    <ul>
        <li><a href="{admin_url}">Admin</a></li>
        <li><a href="{products_url}">Products API</a></li>
    </ul>
        
        """
    
    return HttpResponse(html_content.format(
        admin_url=reverse("admin:index"),
        products_url=reverse("product-list")
        )
    )