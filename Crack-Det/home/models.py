from django.db import models

class Image(models.Model):
    image=models.FileField(upload_to='images')
    name=models.CharField(max_length=20,null=True)

class TextFiles(models.Model):
    text=models.TextField(max_length=50000)
    name=models.CharField(max_length=20,null=True)