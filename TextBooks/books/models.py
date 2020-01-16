from django.db import models

# Create your models here.
class Book(models.Model):
    category = models.CharField(max_length=100)
    image = models.FileField(upload_to='image_books/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='books/')

    def __str__(self):
        return f"{self.name}"
