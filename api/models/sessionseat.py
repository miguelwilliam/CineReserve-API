from django.db import models

class SessionSeat(models.Model):

    class SeatStatus(models.TextChoices):
        AVAILABLE = "available", "Available"
        RESERVED = "reserved", "Reserved"
        PURCHASED = "purchased", "Purchased"

    session = models.ForeignKey("api.Session", on_delete=models.CASCADE, related_name='seats')
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
        constraints = [
            models.UniqueConstraint(
                fields=['session', 'seat'], 
                name='unique_session_seat',
                violation_error_message='This session already have this seat.'
            )
        ]