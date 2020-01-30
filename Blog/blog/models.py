from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    mode = models.BooleanField(default=False)
    description = models.CharField(max_length=100)
    image = models.FileField(upload_to='image_posts/')
    date_created = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return f'{self.user.username}'
