# Generated by Django 3.2.8 on 2022-03-20 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklyacademiccalendar',
            name='week_observations',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='weeklyacademiccalendar',
            name='week_project_typical_activities',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='weeklyacademiccalendar',
            name='week_regular_typical_activities',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
