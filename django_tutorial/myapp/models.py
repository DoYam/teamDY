from django.db import models

# Create your models here.
class Room(models.Model):
    title = models.CharField(max_length=20)
    start_date = models.DateField(auto_now_add=True)
