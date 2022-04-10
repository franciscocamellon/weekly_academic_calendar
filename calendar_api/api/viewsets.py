from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework import viewsets
from calendar_api.api import serializers
from calendar_api import models
from calendar_api.api.filters import AcademicDayFilter, AcademicWeekFilter


class WeeklyAcademicCalendarViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WeeklyAcademicCalendarSerializers
    queryset = models.WeeklyAcademicCalendar.objects.all()


class AcademicDayViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.AcademicDaySerializer
    queryset = models.AcademicDay.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AcademicDayFilter

