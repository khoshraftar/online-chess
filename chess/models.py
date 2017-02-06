from django.db import models
from OnlineChess.classes import chessboard
class users(models.Model):
    name=models.CharField(max_length=32,default='')
    key=models.CharField(max_length=32,default='')
    email=models.EmailField(max_length=48,default='')
    active=models.BooleanField(default=0)
    wins=models.IntegerField(default=0)
    actcode=models.CharField(max_length=16,default='')
    game=models.CharField(default='',max_length=10000)
    turn=models.CharField(default='w',max_length=1)
    class Meta:
        ordering=['wins']