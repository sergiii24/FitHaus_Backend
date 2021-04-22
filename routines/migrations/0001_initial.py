# Generated by Django 3.1.7 on 2021-04-22 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('classes', '0001_initial'),
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('time', models.CharField(choices=[('P', 'Personalitzable'), ('R', 'Ronda circuits'), ('F', 'Fixat')], default='F', max_length=30)),
                ('categories', models.ManyToManyField(to='categories.Category')),
                ('classes', models.ManyToManyField(to='classes.Classes')),
                ('exercises', models.ManyToManyField(to='exercises.Exercise')),
            ],
        ),
    ]
