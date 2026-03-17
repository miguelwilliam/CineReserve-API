from rest_framework import serializers
from api.models import SessionSeat

class SessionSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionSeat
        fields = ['id', 'seat', 'status']