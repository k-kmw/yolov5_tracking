from rest_framework import serializers
from congestion.models import Bus


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = "__all__"
        # fields = ('name', 'description', 'cost')
