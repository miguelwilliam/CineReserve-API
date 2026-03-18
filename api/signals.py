from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from api.models import Seat, Session, SessionSeat, Room

@receiver(post_save, sender=Seat)
def update_total_seats_on_create(sender, instance, **kwargs):
    room = instance.room
    room.total_seats = room.seats.count()
    room.save()


@receiver(post_delete, sender=Seat)
def update_total_seats_on_delete(sender, instance, **kwargs):
    room = instance.room
    room.total_seats = room.seats.count()
    room.save()

@receiver(post_save, sender=Session)
def create_session_seats(sender, instance, created, **kwargs):
    if not created:
        return
    
    seats = instance.room.seats.all()

    session_seats = [
        SessionSeat(
            session=instance,
            seat=seat,
            status=SessionSeat.SeatStatus.AVAILABLE
        )
        for seat in seats
    ]

    SessionSeat.objects.bulk_create(session_seats)
