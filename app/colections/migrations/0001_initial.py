# Generated by Django 3.1.7 on 2021-05-18 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('PredefinedRoutine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('predef_routines', models.ManyToManyField(blank=True, to='PredefinedRoutine.PredefinedRoutine')),
            ],
        ),
    ]
