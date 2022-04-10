from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class WeeklyAcademicCalendar(models.Model):
    week_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    week_alias = models.CharField(max_length=255)
    year = models.IntegerField()
    # week_start = models.DateField()
    week_observations = models.CharField(max_length=255, blank=True, null=True)
    week_regular_typical_activities = models.CharField(max_length=255, blank=True, null=True)
    week_project_typical_activities = models.CharField(max_length=255, blank=True, null=True)
    week_create_date = models.DateTimeField(auto_now_add=True)
    week_update_date = models.DateTimeField(default=None, blank=True, null=True)


class AcademicDay(models.Model):

    class IsSchoolDay(models.TextChoices):
        NORMAL = 'NR', _('Normal')
        RECESS = 'RE', _('Recesso')
        VACATION = 'VA', _('Férias')
        HOLIDAY = 'HO', _('Feriado')

    class TypeOfDegree(models.TextChoices):
        GRADUATION = 'GR', _('Graduação')
        POST_GRADUATION = 'PG', _('Pós Graduação')
        MIT = 'MI', _('Master in Information Technology')
        MBA = 'MB', _('MBAS')

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    day = models.DateField(blank=True, null=True)
    school_day = models.CharField(max_length=2, choices=IsSchoolDay.choices, default=IsSchoolDay.NORMAL)
    observations = models.CharField(max_length=255, blank=True, null=True)
    regular_activity = models.CharField(max_length=255, blank=True, null=True)
    project_activity = models.CharField(max_length=255, blank=True, null=True)
    course = models.CharField(max_length=2, choices=TypeOfDegree.choices, default=TypeOfDegree.GRADUATION)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(default=None, blank=True, null=True)
    # week = models.ForeignKey(WeeklyAcademicCalendar)
