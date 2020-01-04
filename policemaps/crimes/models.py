from django.db import models

# Create your models here.
class Crime(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.FileField(upload_to='crime_images/')
    video = models.FileField(upload_to='crime_videos/')
    display_name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.display_name

class PoliceStation(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    phonenumber = models.CharField(max_length=20)

    def __str__(self):
        return self.phonenumber
