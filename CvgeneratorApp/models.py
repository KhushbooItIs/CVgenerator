from django.db import models

class Profile(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    school=models.CharField(max_length=50)
    degree=models.CharField(max_length=100)
    university=models.CharField(max_length=100)
    summary=models.TextField(max_length=2000)
    previous_work=models.TextField(max_length=1000)
    skil=models.CharField(max_length=200)
