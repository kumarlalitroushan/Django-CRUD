from django.db import models

# Create your models here.

class Books(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=120)
    publisher=models.CharField(max_length=100)
    stock=models.IntegerField(max_length=100)
