from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Movie, Room, Session, Reservation, Seat, SessionSeat

@admin.register(User)
class UserAdmin(BaseUserAdmin):

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Informações pessoais", {"fields": ("username",)}),
        ("Permissões", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Datas importantes", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2"),
        }),
    )

    list_display = ("email", "username", "is_staff")
    search_fields = ("email", "username")
    ordering = ("email",)

# Register your models here.
admin.site.register(Movie)
admin.site.register(Room)
admin.site.register(Session)
admin.site.register(Reservation)
admin.site.register(Seat)
admin.site.register(SessionSeat)