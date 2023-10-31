from django.db import models

# Create your models here.
class Post_data(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()