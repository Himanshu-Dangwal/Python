from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    tags = models.CharField(max_length=60)