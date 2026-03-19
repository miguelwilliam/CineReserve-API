from django.db import models
from django.utils import timezone
from datetime import timedelta

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

    reserved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['session', 'seat'], 
                name='unique_session_seat',
                violation_error_message='This session already have this seat.'
            )
        ]
    
    def is_expired(self):
        if self.status != self.SeatStatus.RESERVED:
            return False
        
        if not self.reserved_at:
            return False
        
        return self.reserved_at < timezone.now() - timedelta(minutes=10)
    
    def release_if_expired(self):
        if self.is_expired():
            self.status = self.SeatStatus.AVAILABLE
            self.reservation = None
            self.reserved_at = None
            self.save()