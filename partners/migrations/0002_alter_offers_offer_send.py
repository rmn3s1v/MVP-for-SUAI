# Generated by Django 5.0.2 on 2024-03-06 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='offer_send',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
