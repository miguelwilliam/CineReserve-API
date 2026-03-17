from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from api.models import Seat

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