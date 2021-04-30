# Generated by Django 3.1.7 on 2021-04-08 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('W', 'Women'), ('X', 'Undefined')], max_length=200)),
                ('birthdate', models.DateField()),
                ('activitiesdone', models.IntegerField(default=0)),
                ('achivements', models.CharField(max_length=200)),
                ('points', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=0)),
                ('objective', models.CharField(max_length=200)),
                ('interestcategories', models.CharField(max_length=200)),
                ('weight', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('imc', models.IntegerField(default=0)),
                ('igc', models.IntegerField(default=0)),
            ],
        ),
    ]
