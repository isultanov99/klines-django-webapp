# Generated by Django 3.2.9 on 2021-12-07 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='Station name')),
                ('lat', models.FloatField(verbose_name='Latitude (dec degrees)')),
                ('lon', models.FloatField(verbose_name='Longitude (dec degrees)')),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
    ]
