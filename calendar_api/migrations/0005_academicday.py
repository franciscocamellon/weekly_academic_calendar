# Generated by Django 4.0.2 on 2022-04-10 00:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_api', '0004_alter_weeklyacademiccalendar_week_update_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDay',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('observations', models.CharField(blank=True, max_length=255, null=True)),
                ('regular_activity', models.CharField(blank=True, max_length=255, null=True)),
                ('project_activity', models.CharField(blank=True, max_length=255, null=True)),
                ('holiday', models.BooleanField()),
                ('course', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
    ]
