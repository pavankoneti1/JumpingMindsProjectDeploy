# Generated by Django 4.2.1 on 2023-06-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elevator', '0009_remove_userrequestmodels_current_floor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrequestmodels',
            name='destination_floor',
            field=models.IntegerField(),
        ),
    ]