# Generated by Django 5.0.1 on 2024-03-27 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_poster', models.URLField()),
                ('name', models.CharField(max_length=255)),
                ('specialties', models.CharField(max_length=255)),
                ('mobile_number', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
