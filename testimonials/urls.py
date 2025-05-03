# testimonials/urls.py
from django.urls import path
from .views import TestimonialListAPIView

urlpatterns = [
    path('api/testimonials/', TestimonialListAPIView.as_view(), name='testimonial-list'),
]
