# Generated by Django 3.1.7 on 2021-06-03 13:01

import computed_property.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('objectives', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalUserDTO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('gender', models.CharField(blank=True, max_length=1)),
                ('birthdate', models.DateField(blank=True)),
                ('activitiesdone', models.IntegerField()),
                ('points', models.IntegerField()),
                ('level', models.CharField(blank=True, max_length=1)),
                ('weight', models.FloatField(default=1)),
                ('height', models.FloatField(default=1)),
                ('imc', models.FloatField(default=1)),
                ('igc', models.FloatField(default=1)),
                ('uid', models.CharField(max_length=200)),
                ('provider', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NormalUserDTO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=1)),
                ('birthdate', models.DateField()),
                ('activitiesdone', models.IntegerField()),
                ('points', models.IntegerField()),
                ('level', models.CharField(blank=True, max_length=1)),
                ('weight', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('height', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('imc', models.FloatField(default=1)),
                ('igc', models.FloatField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True, validators=[django.core.validators.MinLengthValidator(4)])),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('W', 'Women'), ('X', 'Undefined')], max_length=1)),
                ('birthdate', models.DateField(null=True)),
                ('activitiesdone', computed_property.fields.ComputedIntegerField(compute_from='calc_routines', editable=False)),
                ('points', models.IntegerField(default=0)),
                ('level', models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced')], max_length=1)),
                ('strengthtrainings', models.IntegerField(default=0)),
                ('cardiotrainings', models.IntegerField(default=0)),
                ('yogatrainings', models.IntegerField(default=0)),
                ('stretchingtrainings', models.IntegerField(default=0)),
                ('rehabilitationtrainings', models.IntegerField(default=0)),
                ('pilatestrainings', models.IntegerField(default=0)),
                ('weight', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('height', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('imc', computed_property.fields.ComputedFloatField(compute_from='calc_imc', default=1, editable=False)),
                ('igc', computed_property.fields.ComputedFloatField(compute_from='calc_igc', default=1, editable=False)),
                ('categories', models.ManyToManyField(to='categories.Category')),
                ('objectives', models.ManyToManyField(to='objectives.Objective')),
            ],
        ),
        migrations.CreateModel(
            name='ExternUser',
            fields=[
                ('uid', models.CharField(max_length=200)),
                ('provider', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='extern_user', serialize=False, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='NormalUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=200, validators=[django.core.validators.MinLengthValidator(8), users.validators.correct_pwd])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='normal_user', to='users.user')),
            ],
        ),
    ]
