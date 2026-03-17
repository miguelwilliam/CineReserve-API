from django.db import models
    
class Room(models.Model):
    name = models.CharField(max_length=50)
    total_seats = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name