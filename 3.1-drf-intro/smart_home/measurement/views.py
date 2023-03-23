from psycopg2 import OperationalError
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, \
    ListAPIView
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class CreateSensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def create_sensor(self, request, *args, **kwargs):
        try:
            sensor_name = request.POST.get('sensor_name')
            description = request.POST.get('description')
            Sensor(sensor_name=sensor_name, descriptions=description).save()
            return Response({'status': 'Датчик добавлен'})
        except OperationalError as e:
            return Response({'status': f'Произошла ошибка{e}'})


class ChangeSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class CreateMeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def create_measurement(self, request):
        try:
            sensor = request.POST.get('sensor')
            temperature = request.POST.get('temperature')
            MeasurementSerializer(sensor=sensor, temperature=temperature).save()
            return Response({'status': 'Измерение добавлено.'})
        except OperationalError as e:
            return Response({'status': f'Произошла ошибка{e}'})


class SensorDetailsView(RetrieveAPIView):
    queryset = Sensor.objects.all().prefetch_related('sensor')
    serializer_class = SensorDetailSerializer
