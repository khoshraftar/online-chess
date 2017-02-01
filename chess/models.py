from django.db import models
class users(models.Model):
    name=models.CharField(max_length=32)
    key=models.CharField(max_length=32)
    email=models.CharField(max_length=48)
    active=models.BooleanField()
    wins=models.IntegerField()
    class Meta:
        ordering=['wins']