from rest_framework import serializers
from .models import Wigs

class WigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wigs
        fields = '__all__'