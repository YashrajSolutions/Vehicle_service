# Generated by Django 5.0.3 on 2024-03-19 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle_service', '0002_alter_vehicle_details_vehicle_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle_details',
            name='user_id',
            field=models.CharField(max_length=16),
        ),
    ]
