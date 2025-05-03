from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    publish_date = models.DateField()
    read_time = models.CharField(max_length=10)  # Example: "5 min read"
    author_image = models.ImageField(upload_to='authors/', null=True, blank=True)
    background_image = models.ImageField(upload_to='backgrounds/', null=True, blank=True)  # New field for background image

    def __str__(self):
        return self.title
