# Generated by Django 3.1.7 on 2021-05-31 22:02

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
            name='HealthData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', computed_property.fields.ComputedIntegerField(compute_from='calc_weight', default=1, editable=False)),
                ('height', computed_property.fields.ComputedIntegerField(compute_from='calc_height', default=1, editable=False)),
                ('imc', computed_property.fields.ComputedFloatField(compute_from='calc_imc', editable=False)),
                ('igc', computed_property.fields.ComputedFloatField(compute_from='calc_igc', editable=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'ordering': ['id'],
                'unique_together': {('user', 'date')},
            },
        ),
    ]
