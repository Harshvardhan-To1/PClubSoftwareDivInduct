# Generated by Django 5.0.1 on 2024-01-29 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('W2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='present',
            name='Date',
            field=models.DateField(),
        ),
    ]
