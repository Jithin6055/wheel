# Generated by Django 5.1 on 2024-09-28 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='dropoff_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dropoffs', to='main.location'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='pickup_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pickups', to='main.location'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
