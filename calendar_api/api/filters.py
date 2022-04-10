from rest_framework import generics
from django_filters import rest_framework as filters
import django_filters
from django_filters.widgets import DateRangeWidget
from calendar_api import models


class AcademicDayFilter(filters.FilterSet):
    day = filters.DateFilter()
    week = filters.DateFromToRangeFilter()
    is_holiday = filters.CharFilter(field_name='school_day')
    course = filters.CharFilter(field_name='course')
    start_date = filters.DateFilter(field_name='day', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='day', lookup_expr='lte')

    class Meta:
        model = models.AcademicDay
        fields = '__all__'


class AcademicWeekFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name='day', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='day', lookup_expr='lte')

    class Meta:
        model = models.AcademicDay
        fields = ['day']
