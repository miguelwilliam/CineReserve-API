from django.db import models

class Session(models.Model):
    movie = models.ForeignKey("api.Movie", on_delete=models.CASCADE)
    room = models.ForeignKey("api.Room", on_delete=models.CASCADE)
    start_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie} - {self.start_time}"