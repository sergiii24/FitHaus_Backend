# Generated by Django 3.1.7 on 2021-06-03 13:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseDTO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='E', max_length=30)),
                ('name', models.CharField(default='', max_length=50)),
                ('description', models.CharField(max_length=500, null=True)),
                ('age', models.CharField(default='A', max_length=30)),
                ('difficulty', models.CharField(default='M', max_length=30)),
                ('length', models.IntegerField(null=True)),
                ('pre', models.ImageField(null=True, upload_to='activities_images')),
                ('muscleimage', models.ImageField(default=None, upload_to='exercise_images')),
                ('videotutorial', models.FileField(default=None, upload_to='exercise_videos')),
                ('videoexercise', models.FileField(default=None, upload_to='exercise_videos')),
                ('muscle', models.CharField(default='Bi', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('type', models.CharField(choices=[('E', 'Exercise'), ('C', 'Class')], default='E', max_length=30)),
                ('name', models.CharField(default='', max_length=50, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=500, null=True)),
                ('age', models.CharField(choices=[('K', 'Kid'), ('T', 'Teenager'), ('A', 'Adult'), ('E', 'Elder')], default='A', max_length=30)),
                ('difficulty', models.CharField(choices=[('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard')], default='M', max_length=30)),
                ('length', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('pre', models.ImageField(null=True, upload_to='activities_images')),
                ('muscleimage', models.ImageField(default=None, upload_to='exercise_images')),
                ('videotutorial', models.FileField(default=None, upload_to='exercise_videos')),
                ('videoexercise', models.FileField(default=None, upload_to='exercise_videos')),
                ('muscle', models.CharField(choices=[('Bi', 'Biceps'), ('Tr', 'Triceps'), ('Fa', 'Forearm'), ('Ch', 'Chest'), ('Sh', 'Shoulder'), ('Do', 'Dorsal'), ('Gl', 'Gluteus'), ('Fe', 'Femoral'), ('Qu', 'Quadriceps'), ('Ca', 'Calf'), ('Co', 'Core')], default='Bi', max_length=200)),
                ('categories', models.ManyToManyField(to='categories.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
