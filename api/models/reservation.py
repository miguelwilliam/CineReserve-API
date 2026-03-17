from django.db import models

class Reservation(models.Model):

    class ReservationStatus(models.TextChoices):
        PENDING = "pending", "Pending"
        CONFIRMED = "confirmed", "Confirmed"
        CANCELLED = "cancelled", "Cancelled"

    user = models.ForeignKey("api.User", on_delete=models.CASCADE)
    session = models.ForeignKey("api.Session", on_delete=models.CASCADE)

    status = models.CharField(
        max_length=10,
        choices=ReservationStatus.choices,
        default=ReservationStatus.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)