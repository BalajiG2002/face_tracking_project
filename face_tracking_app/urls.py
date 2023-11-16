# face_tracking_app/urls.py
from django.urls import path
from .views import face_detection_results

urlpatterns = [
    path('', face_detection_results, name='detection_results'),
]
