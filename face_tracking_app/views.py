# face_tracking_app/views.py
from django.shortcuts import render
from .models import DetectedFace

def face_detection_results(request):
    detected_faces = DetectedFace.objects.all()
    return render(request, 'face_tracking_app/detection_results.html', {'detected_faces': detected_faces})
