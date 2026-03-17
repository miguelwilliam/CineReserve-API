from rest_framework import serializers
from api.models import Session
from api.serializers.session_seat import SessionSeatSerializer

class SessionSerializer(serializers.ModelSerializer):
    seats = SessionSeatSerializer(many=True, read_only=True)

    class Meta:
        model = Session
        fields = '__all__'