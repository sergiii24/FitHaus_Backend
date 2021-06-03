# Generated by Django 3.1.7 on 2021-06-03 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exercises', '0001_initial'),
        ('categories', '0001_initial'),
        ('objectives', '0001_initial'),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredefinedRoutine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('time', models.CharField(choices=[('P', 'Personalitzable'), ('R', 'Ronda circuits'), ('F', 'Fixat')], default='F', max_length=30)),
                ('age', models.CharField(choices=[('K', 'Kid'), ('T', 'Teenager'), ('A', 'Adult'), ('E', 'Elder')], default='A', max_length=30)),
                ('level', models.CharField(choices=[('P', 'Principiate'), ('I', 'Intermediate'), ('A', 'Advanced')], default='P', max_length=30)),
                ('equipment', models.CharField(choices=[('W', 'Without'), ('HM', 'HomeMaterial'), ('K', 'Kettlebelt'), ('B', 'Bodyweight'), ('D', 'Dumpbell'), ('RB', 'ResistanceBand'), ('RL', 'ResistanceLoop'), ('FR', 'FoamRoller')], default='W', max_length=30)),
                ('impact', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], default='M', max_length=30)),
                ('image', models.ImageField(default=None, upload_to='predef_routines_images')),
                ('categories', models.ManyToManyField(default=None, to='categories.Category')),
                ('classes', models.ManyToManyField(blank=True, default=None, to='classes.Class')),
                ('exercises', models.ManyToManyField(blank=True, default=None, to='exercises.Exercise')),
                ('objective', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='objectives.objective')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
