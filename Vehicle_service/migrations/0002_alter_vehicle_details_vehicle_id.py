# Generated by Django 5.0.3 on 2024-03-18 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle_details',
            name='vehicle_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]