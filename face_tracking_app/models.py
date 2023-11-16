# face_tracking_app/models.py
from django.db import models


class DetectedFace(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    x_position = models.IntegerField()
    y_position = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
