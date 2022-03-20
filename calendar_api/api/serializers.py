from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from calendar_api import models

class WeeklyAcademicCalendarSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.WeeklyAcademicCalendar
        fields = '__all__'