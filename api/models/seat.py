from django.db import models

class Seat(models.Model):
    room = models.ForeignKey("api.Room", on_delete=models.CASCADE, related_name='seats')
    row = models.CharField(max_length=5)
    number = models.IntegerField()

    def __str__(self):
        return f"{self.row}{self.number}"