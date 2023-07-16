from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):

    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name + '' + self.description


class Measurement(models.Model):

    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
    temperature = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    changed_at = models.DateTimeField(auto_now=True, null=True)
