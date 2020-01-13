from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=20)
    image = models.FileField(upload_to="images/")
    def __str__(self):
        return f'{self.user.username}'

class Friends(models.Model):
    friend = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="friends_set")
    name = models.CharField(max_length=100)
    accepted = models.BooleanField(default=False)
