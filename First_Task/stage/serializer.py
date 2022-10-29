
from .models import Me
from rest_framework import serializers


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Me
        fields=['slackUsername','backend','age','bio']
