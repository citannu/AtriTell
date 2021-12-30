from django.db import models
from uuid import uuid4

class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.CharField(max_length=30, blank=True)
    creation_date = models.DateField(auto_now_add=True)
    
    random_url_id = models.UUIDField(default=uuid4)


class Note(models.Model):
    pass
