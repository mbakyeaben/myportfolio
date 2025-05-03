from django.urls import path
from .views import BlogPostListCreateView, BlogPostRetrieveUpdateDestroyView

urlpatterns = [
    path('api/blog-posts/', BlogPostListCreateView.as_view(), name='blogpost-list-create'),
    path('api/blog-posts/<int:pk>/', BlogPostRetrieveUpdateDestroyView.as_view(), name='blogpost-detail'),
]
