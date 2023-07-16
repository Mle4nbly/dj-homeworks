from django.urls import path
from .views import SensorsView, CreateSensorView, CreateMeasurementView, SensorView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<id>/', SensorView.as_view()),
    path('measurements/', CreateMeasurementView.as_view()),
    path('sensors/', CreateSensorView.as_view())
]
