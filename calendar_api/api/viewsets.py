from rest_framework import viewsets
from calendar_api.api import serializers
from calendar_api import models

class WeeklyAcademicCalendarViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WeeklyAcademicCalendarSerializers
    queryset = models.WeeklyAcademicCalendar.objects.all()
