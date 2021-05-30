# Generated by Django 3.1.7 on 2021-05-30 17:42

import django.core.validators
from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('objectives', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True, validators=[django.core.validators.MinLengthValidator(4)])),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(8), users.validators.correct_pwd])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('W', 'Women'), ('X', 'Undefined')], max_length=1)),
                ('birthdate', models.DateField()),
                ('activitiesdone', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('level', models.CharField(blank=True, choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced')], max_length=1)),
                ('weight', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(1)])),
                ('height', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(1)])),
                ('categories', models.ManyToManyField(blank=True, to='categories.Category')),
                ('objectives', models.ManyToManyField(blank=True, to='objectives.Objective')),
            ],
        ),
    ]
