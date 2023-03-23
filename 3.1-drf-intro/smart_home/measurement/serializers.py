from rest_framework import serializers

from .models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'sensor_name', 'descriptions']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(source='sensor', read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'sensor_name', 'descriptions', 'measurements']
