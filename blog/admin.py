from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'content', 'author', 'publish_date', 'read_time','author_image', 'background_image')
    search_fields = ('title', 'category', 'author')
    list_filter = ('category', 'publish_date')
    date_hierarchy = 'publish_date'
    ordering = ('-publish_date',)
