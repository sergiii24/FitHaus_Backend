# Generated by Django 3.1.7 on 2021-06-01 13:14

import computed_property.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('PredefinedRoutine', '0001_initial'),
        ('users', '0001_initial'),
        ('CustomRoutine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hInici', models.TimeField()),
                ('hFi', models.TimeField()),
                ('totalTime', computed_property.fields.ComputedIntegerField(compute_from='calc_hours', editable=False)),
                ('done', models.BooleanField()),
                ('shared', models.BooleanField()),
                ('customroutine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CustomRoutine.customroutine')),
                ('predefinedroutine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PredefinedRoutine.predefinedroutine')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
