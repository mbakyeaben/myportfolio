from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'category', 'content', 'author', 'publish_date', 'read_time', 'author_image', 'background_image']
