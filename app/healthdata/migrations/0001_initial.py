# Generated by Django 3.1.7 on 2021-06-03 13:01

import computed_property.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthDataDTO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=None)),
                ('weight', models.FloatField(default=1)),
                ('height', models.FloatField(default=1)),
                ('imc', models.FloatField(default=1)),
                ('igc', models.FloatField(default=1)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='HealthData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', computed_property.fields.ComputedFloatField(compute_from='calc_weight', default=1, editable=False)),
                ('height', computed_property.fields.ComputedFloatField(compute_from='calc_height', default=1, editable=False)),
                ('imc', computed_property.fields.ComputedFloatField(compute_from='calc_imc', default=1, editable=False)),
                ('igc', computed_property.fields.ComputedFloatField(compute_from='calc_igc', default=1, editable=False)),
                ('date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
