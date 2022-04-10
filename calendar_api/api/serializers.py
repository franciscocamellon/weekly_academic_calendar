from rest_framework import serializers
from calendar_api import models


class WeeklyAcademicCalendarSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.WeeklyAcademicCalendar
        fields = '__all__'


class AcademicDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AcademicDay
        fields = '__all__'
