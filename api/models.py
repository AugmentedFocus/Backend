from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Otros campos específicos del perfil del usuario

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # Otros detalles del curso, como duración, instructor, etc.

class Unit(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="units")
    title = models.CharField(max_length=255)
    content = models.TextField()

class Activity(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="activities")
    name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()

class Grade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    score = models.FloatField()

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    event_date = models.DateTimeField()
