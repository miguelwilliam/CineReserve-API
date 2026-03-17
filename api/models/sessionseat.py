from django.db import models

class SessionSeat(models.Model):

    class SeatStatus(models.TextChoices):
        AVAILABLE = "available", "Available"
        RESERVED = "reserved", "Reserved"
        PURCHASED = "purchased", "Purchased"

    session = models.ForeignKey("api.Session", on_delete=models.CASCADE)
    seat = models.ForeignKey("api.Seat", on_delete=models.CASCADE)

    status = models.CharField(
        max_length=10,
        choices=SeatStatus.choices,
        default=SeatStatus.AVAILABLE
    )

    reservation = models.ForeignKey(
        "api.Reservation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        unique_together = ("session", "seat")