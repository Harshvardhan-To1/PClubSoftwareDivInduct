# Generated by Django 5.0.1 on 2024-01-29 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Present',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll_No', models.TextField(max_length=122)),
                ('Date', models.TextField(max_length=122)),
                ('Password', models.TextField(max_length=122)),
            ],
        ),
    ]
