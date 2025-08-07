from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50,default="Test")
    email = models.EmailField(unique=True,default="test@example.com")  # better validation and uniqueness
    age = models.PositiveIntegerField(default=25)     # avoids negative ages
    date_joined = models.DateTimeField(auto_now_add=True)  # clearer field name

    def __str__(self):
        return f"{self.name} ({self.email})"