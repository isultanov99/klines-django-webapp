# Generated by Django 3.2.9 on 2021-12-16 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('num', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('timetable', models.JSONField(default=dict)),
                ('days', models.JSONField(default=list)),
                ('from_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_set', to='stations.station')),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stations.line')),
                ('to_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_set', to='stations.station')),
            ],
            options={
                'ordering': ['line', 'from_station', 'num'],
            },
        ),
    ]