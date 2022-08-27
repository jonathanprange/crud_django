from rest_framework import serializers
from region import models

class RegionSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Regions
        fields = '__all__'
