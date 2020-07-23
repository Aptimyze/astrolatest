# Generated by Django 3.0 on 2020-07-20 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_dailypanchang'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolarCycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('sunrise', models.TimeField()),
                ('sunset', models.TimeField()),
                ('moonsign', models.CharField(max_length=50)),
                ('moonrise', models.TimeField()),
                ('moonset', models.TimeField()),
                ('ritu', models.CharField(max_length=50)),
                ('astroprofile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Astro_Profile')),
            ],
        ),
    ]
