# Generated by Django 5.1.2 on 2025-03-04 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.IntegerField(blank=True, help_text='Skill level (0-100)', null=True),
        ),
    ]
