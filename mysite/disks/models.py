from django.db import models

# Create your models here.

class track(models.Model):
    name = models.CharField(max_length=50)
    composer = models.CharField(max_length=100, null = True)
    milliseconds = models.IntegerField()
    unitPrice = models.DecimalField(decimal_places=2, max_digits = 10)
    album = models.ForeignKey('Album', on_delete= models.CASCADE)
    bytes = models.IntegerField()
    
class album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
       

class artist(models.Model):
    name = models.CharField(max_length=50)