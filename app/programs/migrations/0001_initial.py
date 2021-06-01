# Generated by Django 3.1.7 on 2021-05-31 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('PredefinedRoutine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('level', models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced')], default='B', max_length=1)),
                ('weeks', models.IntegerField(default=0)),
                ('predef_routines', models.ManyToManyField(blank=True, to='PredefinedRoutine.PredefinedRoutine')),
            ],
            options={
                'unique_together': {('name', 'level')},
            },
        ),
    ]
