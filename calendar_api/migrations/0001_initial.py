# Generated by Django 3.2.8 on 2022-03-20 13:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyAcademicCalendar',
            fields=[
                ('week_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('week_alias', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('week_start', models.DateField()),
                ('week_observations', models.CharField(max_length=255)),
                ('week_regular_typical_activities', models.CharField(max_length=255)),
                ('week_project_typical_activities', models.CharField(max_length=255)),
                ('week_create_date', models.DateField(auto_now_add=True)),
                ('week_update_date', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
    ]
