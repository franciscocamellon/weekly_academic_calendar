# Generated by Django 3.2.8 on 2022-03-20 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_api', '0003_alter_weeklyacademiccalendar_week_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklyacademiccalendar',
            name='week_update_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
