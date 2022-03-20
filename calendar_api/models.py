from pyexpat import model
from uuid import uuid4
from django.db import models

# Create your models here.

class WeeklyAcademicCalendar(models.Model):

    week_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    week_alias = models.CharField(max_length=255)
    year = models.IntegerField()
    week_start = models.DateField()
    week_observations = models.CharField(max_length=255, blank=True, null=True)
    week_regular_typical_activities = models.CharField(max_length=255, blank=True, null=True)
    week_project_typical_activities = models.CharField(max_length=255, blank=True, null=True)
    week_create_date = models.DateTimeField(auto_now_add=True)
    week_update_date = models.DateTimeField(default=None, blank=True, null=True)


