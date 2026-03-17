from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Movie, Room, Session, Reservation, Seat, SessionSeat

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Movie)
admin.site.register(Room)
admin.site.register(Session)
admin.site.register(Reservation)
admin.site.register(Seat)
admin.site.register(SessionSeat)