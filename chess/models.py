from django.db import models
class users(models.Model):
    name=models.CharField(max_length=32,default='')
    key=models.CharField(max_length=32,default='')
    email=models.EmailField(max_length=48,default='')
    active=models.BooleanField(default=0)
    wins=models.IntegerField(default=0)
    actcode=models.CharField(max_length=16,default='')
    class Meta:
        ordering=['wins']