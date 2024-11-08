# products/pagination.py
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

# Custom PageNumberPagination
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10  # Items per page
    page_query_param = 'page'  # URL parameter for page number
    page_size_query_param = 'page_size'  # URL parameter for page size
    max_page_size = 50  # Max items per page

# Custom LimitOffsetPagination
class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10  # Default limit per page
    limit_query_param = 'limit'  # URL parameter for limit
    offset_query_param = 'offset'  # URL parameter for offset
    max_limit = 50  # Maximum limit

# Custom CursorPagination
class CustomCursorPagination(CursorPagination):
    page_size = 10  # Items per page
    ordering = '-created_at'  # Order by this field (descending by default)
    cursor_query_param = 'cursor'  # URL parameter for cursor
