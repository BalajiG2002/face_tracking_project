# face_tracking_app/management/commands/face_detection.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from face_tracking_app.models import DetectedFace
import cv2

class Command(BaseCommand):
    help = 'Detect faces in video feed and save to database'

    def handle(self, *args, **options):
        
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

                # Save detected face to the database
                DetectedFace.objects.create(
                    name="John Doe",  # Hardcoded name for now
                    x_position=x,
                    y_position=y,
                    width=w,
                    height=h
                )

            cv2.imshow('Face Detection', frame)

            if cv2.waitKey(500) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        self.stdout.write(self.style.SUCCESS('Script executed successfully'))
