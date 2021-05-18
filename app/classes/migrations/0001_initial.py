# Generated by Django 3.1.7 on 2021-05-18 06:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('E', 'Exercise'), ('C', 'Class')], default='E', max_length=30)),
                ('name', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('age', models.CharField(choices=[('K', 'Kid'), ('T', 'Teenager'), ('A', 'Adult'), ('E', 'Elder')], default='A', max_length=30)),
                ('difficulty', models.CharField(choices=[('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard')], default='M', max_length=30)),
                ('length', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('pre', models.ImageField(null=True, upload_to='activities_images')),
                ('videoclass', models.FileField(default=None, upload_to='class_videos')),
                ('trainer', models.CharField(max_length=30)),
                ('workarea', models.CharField(choices=[('UB', 'Upper Body'), ('LB', 'Lower Body'), ('FB', 'Full Body'), ('C', 'Core')], default='FB', max_length=200)),
                ('categories', models.ManyToManyField(to='categories.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
