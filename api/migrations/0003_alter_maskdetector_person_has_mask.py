# Generated by Django 3.2 on 2021-05-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_maskdetector_person_has_mask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maskdetector',
            name='person_has_mask',
            field=models.BooleanField(),
        ),
    ]
