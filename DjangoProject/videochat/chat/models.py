from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    room_name = models.CharField(max_length=255,unique=True)
    allowed_users= models.PositiveIntegerField(default=1)

    
    def __str__(self):
        return self.room_name