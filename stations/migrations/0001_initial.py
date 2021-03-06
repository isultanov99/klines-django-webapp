# Generated by Django 3.2.9 on 2021-12-16 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Station name')),
                ('lat', models.FloatField(verbose_name='Latitude (dec degrees)')),
                ('lon', models.FloatField(verbose_name='Longitude (dec degrees)')),
                ('slug', models.SlugField()),
                ('line', models.ManyToManyField(to='stations.Line')),
            ],
        ),
    ]
